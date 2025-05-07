from media.Engage import Engage
from spread.SpreadSheet import SpreadSheet
from salesforce.SalesforceJobSeekerRecord import SalesforceJobSeekerRecord

# engage = Engage()
# print('ログイン完了')

applicant_data = {'engage0': {'last_name': 'テスト', 'first_name': 'タロウ', 'last_name_kana': 'テスト', 'first_name_kana': 'タロウ', 'entry_date': '2025/05/01', 'email': 'taro@tset.com', 'phone': '07037933505', 'gender': '女性', 'birth_day': '1999/10/13', 'prefecture': '北海道', 'media_name': 'engage', 'enrollment_status': '離職'}, 'engage1': {'last_name': 'テスト', 'first_name': '花子', 'last_name_kana': 'テスト', 'first_name_kana': 'ハナコ', 'entry_date': '2025/05/01', 'email': 'test@taro.com', 'phone': '09057315757', 'gender': '男性', 'birth_day': '1995/12/11', 'prefecture': '福岡県', 'media_name': 'engage', 'enrollment_status': '在職'}}

# applicant_data = engage.get_applicant_data()
SpreadSheet().write_to_spreadsheet(applicant_data)

# salesforce_job_seeker_record = SalesforceJobSeekerRecord()
# salesforce_job_seeker_record.store(applicant_data)



# engage.logout()
# print('終了')
