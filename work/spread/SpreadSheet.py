from datetime import date, datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
import const
from messages.SuccessMessage import SuccessMessage

class SpreadSheet():
    # 姓名を結合してフルネームを取得するメソッドを定義
    def get_full_name(self, last_name: str, first_name: str) -> str:
        return f"{last_name} {first_name}"

    # スプレッドシートに書き込むためのメソッドを定義
    def calculate_age_and_format_date(self, birthdate_str: str) -> int:
        # スラッシュ区切りの日付をパース    
        birthdate = datetime.strptime(birthdate_str, "%Y/%m/%d").date()
        today = date.today()

        # 年齢を計算
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        return age

    # 日付をハイフン区切りに変換
    def convert_to_date_format(self, birthdate_str: str) -> str:
        # スラッシュ区切りで受け取り、ハイフン区切りで返す
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y/%m/%d").date()
            return birthdate.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("入力された日付の形式が不正です（例: '1981/04/04'）")

    # 書類選考の合否を判定
    def isDocumentScreeningPassed(self, age: int, name: str) -> tuple:
        age_limit = int(const.SPREAD_SHEET_KPI_AGE_LIMIT)
        if age <= age_limit:
            if self.check_name_type(name) == "漢字氏名":
                return '○', ''
            return '×', '外国籍'
        else:
            return '×', '年齢'
    
    # 氏名のタイプを判定
    # 漢字氏名、カタカナ氏名、その他の3つのタイプを判定
    def check_name_type(self, name):
        # 漢字が含まれているかをチェック
        if re.search(r'[一-龯]', name):
            return "漢字氏名"
        
        # カタカナが含まれているかをチェック
        elif re.search(r'[ア-ン]', name):
            return "カタカナ氏名"
        
        # それ以外のケース
        else:
            return "不明"
    
    # 地域を判定
    def judge_region(self, prefecture: str) -> str:
        match prefecture:
            case "北海道":
                return "札幌"
            case "福岡県":
                return "福岡"
            case "東京都":
                return "東京"
            case "大阪府":
                return "大阪"
            case _:
                return "その他"

    # applicant_dataを受け取り、必要な情報を抽出して配列に変換
    def convert_to_array(self, applicant_data: dict) -> list:
        # tmp_listを受け取り、必要な情報を抽出して配列に変換
        values = []

        for data in applicant_data:
            value = []
            # 年齢
            age = self.calculate_age_and_format_date(applicant_data[data]['birth_day'])
            # 氏名
            full_name = self.get_full_name(applicant_data[data]['last_name'], applicant_data[data]['first_name'])
            value.append(full_name)
            # ステータス
            value.append(const.SPREAD_SHEET_KPI_DEFAULT_STATUS)
            # 年齢
            value.append(age)
            # 性別
            value.append(applicant_data[data]['gender'])
            # 地域
            region = self.judge_region(applicant_data[data]['prefecture'])
            value.append(region)
            # 在籍状況
            value.append(applicant_data[data]['enrollment_status'])
            # 流入経路
            value.append(applicant_data[data]['media_name'])
            # 応募日程
            entry_date = self.convert_to_date_format(applicant_data[data]['entry_date'])
            value.append(entry_date)
            # 入社希望（空白でOK）
            value.append('')
            # 書類選考：結果・理由
            doc_screening_result, doc_screening_reason = self.isDocumentScreeningPassed(age, full_name)
            value.append(doc_screening_result)
            value.append(doc_screening_reason)
            values.append(value)

        return values
    
    # スプレッドシートに書き込むためのメソッドを定義
    def write_to_spreadsheet(self, values: list) -> None:
        # スプレッドシートAPIのスコープ定義
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # 認証情報の読み込み
        credentials = ServiceAccountCredentials.from_json_keyfile_name("/work/credentials.json", scope)

        # 認証してクライアント作成
        client = gspread.authorize(credentials)

        # スプレッドシートを開く
        spreadsheet = client.open_by_key(const.SPREAD_SHEET_KPI_ID)

        # ワークシートの選択
        sheet = spreadsheet.worksheet(const.SPREAD_SHEET_KPI_WORKSHEET_NAME)

        # C列の最終行の次の行インデックスを取得
        next_row = len(sheet.col_values(3)) + 1  # 3はC列

        # 書き込むデータを変換
        convert_values = self.convert_to_array(values)

        # 書き込むセル範囲を作成（行数に応じて変動）
        end_row = next_row + len(convert_values) - 1
        cell_range = f"C{next_row}:M{end_row}"

        # データ書き込み（形式を反映させる）
        sheet.update(convert_values, cell_range, value_input_option="USER_ENTERED")
        
        # 書き込み完了メッセージ
        # print(f"スプレッドシートに{len(convert_values)}件のデータを書き込みました。")
        print(SuccessMessage.SPREAD_SHEET_WRITE_SUCCESS())
