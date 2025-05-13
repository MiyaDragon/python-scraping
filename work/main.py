from media.Engage import Engage
from spread.SpreadSheet import SpreadSheet
from salesforce.SalesforceJobSeekerRecord import SalesforceJobSeekerRecord
from messages.LogMessage import LogMessage

engage = Engage()

applicant_data = engage.get_applicant_data()

if applicant_data == {}:
    print(LogMessage.NOT_APPLICANT)
    exit()

# 応募者データをスプレッドシートに書き込む
SpreadSheet().write_to_spreadsheet(applicant_data)
# 応募者データをSalesforceに登録する
salesforce_job_seeker_record = SalesforceJobSeekerRecord()
salesforce_job_seeker_record.store(applicant_data)
