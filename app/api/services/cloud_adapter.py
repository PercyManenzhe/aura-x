# Simple mock for Huawei Cloud interaction
class HuaweiCloudAdapter:
    def upload_data(self, data):
        print(f"☁ Uploading data to Huawei Cloud: {data}")
        return True

    def fetch_content(self, content_id):
        print(f"☁ Fetching content {content_id} from Huawei Cloud")
        return f"Simulated content {content_id}"
