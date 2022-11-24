from cloudant.client import Cloudant
client=Cloudant.iam('3baf147f-3fb3-4aa4-ac12-62200863d3c4-bluemix','aTgtrUrqUdiw2rxNYMrFMa7qFqf34tDif5hpAE7JPjxs',connect=True)
my_database=client.create_database('my-database')