import platforms

aws = platforms.AWS()
print(aws.calculatePrice(1001339,30000,2048))

google = platforms.Google()
print(google.calculatePrice(1001339,30000,2048))

azure = platforms.Azure()
print(azure.calculatePrice(1001339,30000,2048))

ibm = platforms.IBM()
print(ibm.calculatePrice(1001339,30000,2048))