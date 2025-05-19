from media import Engage, Mynavi
from spread.SpreadSheet import SpreadSheet
from salesforce.SalesforceJobSeekerRecord import SalesforceJobSeekerRecord
from messages.LogMessage import LogMessage

# 応募者データを取得する関数
def collect_applicant_data(media_classes):
    merged_data = {}
    for media_cls in media_classes:
        media = media_cls()
        data = media.get_applicant_data()
        if data:
            merged_data.update(data)
    return merged_data

# 媒体をここで定義するだけでOK
media_classes = [Engage, Mynavi]

applicant_data = collect_applicant_data(media_classes)

# 応募者データが空の場合は終了
if applicant_data == {}:
    print(LogMessage.NOT_APPLICANT())
    exit()

# 応募者データをスプレッドシートに書き込む
SpreadSheet().write_to_spreadsheet(applicant_data)
# 応募者データをSalesforceに登録する
salesforce_job_seeker_record = SalesforceJobSeekerRecord()
salesforce_job_seeker_record.store(applicant_data)
