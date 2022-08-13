# This function is written to get list of EC2 instances as Dictionary Object in Python
import boto3
ec2 = boto3.client('ec2',region_name="us-east-1")

ec2_dict=ec2.describe_instances()
print("ec2_dict type is",type(ec2_dict))
print("ec2_dict is",ec2_dict)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances
# Below is the Example Python Dictionary response for 'ec2.describe_instances()'




'''
test_dict=
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketByTags",
                "s3:GetBucketLocation",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::aws-devops-testbucket",
                "arn:aws:s3:::aws-devops-testbucket/*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:GetAccountPublicAccessBlock",
                "s3:HeadBucket"
            ],
            "Resource": "*"
        }
    ]
}

instance_id=instances['Instances'][0]['InstanceId']
instance_state=instances['Instances'][0]['State']['Name']
instance_tags=instances['Instances'][0]['Tags']

InstanceId_Value = ec2_dictionary['Reservations'][0]['Instances'][0]['InstanceId']
InstanceState_Value = ec2_dictionary['Reservations'][0]['Instances'][0]['State']['Name']

instance_id = ec2_dictionary['Reservations'][0]['Instances'][0]['InstanceId']
instance_state = ec2_dictionary['Reservations'][0]['Instances'][0]['State']['Name']


ec2_dictionary['Reservations'][0]['Instances'][0]['InstanceId']
ec2_dictionary['Reservations'][0]['Instances'][0]['State']['Name']




ec2_dictionary['Reservations'][0]['Instances'][0]['State']['Name']

test_dir = {
	"Reservations": [
		{"Instances1":['one'], 'Groups1': ['two'] },
		{"Instances2":['three'], 'Groups2': ['four'] },
		{"Instances3":[], 'Groups3': [] }
		]
}

test_dir['Reservations'][0]['Instances1'][0] => 'one'



















test_dir['Reservations'] => List => [{"Instances1":[], 'Groups1': [] },{"Instances2":[], 'Groups2': [] },{"Instances3":[], 'Groups3': [] }]
test_dir['Reservations'][0] => {"Instances1":[], 'Groups1': [] }
test_dir['Reservations'][0]['Instances1'] => []


instance_id = ec2_dictionary['Reservations'][0]['Instances'][0]['InstanceId']
instance_state = ec2_dictionary['Reservations'][0]['Instances'][0]['State']['Name']
ec2_dictionary=
{
	'Reservations': 
	[ 
		{
		'Groups': [],
		'Instances': [{
			'AmiLaunchIndex': 0,
			'ImageId': 'ami-08f63db601b82ff5f',
			'InstanceId': 'i-0f998cd8f0c4d7765',
			'InstanceType': 't2.micro',
			'KeyName': 'aws-linux-mumbai',
			'LaunchTime': datetime.datetime(2020, 12, 13, 3, 54, 1, tzinfo = tzlocal()),
			'Monitoring': {
				'State': 'disabled'
			},
			'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
			'PrivateIpAddress': '172.31.29.10',
			'ProductCodes': [],
			'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
			'PublicIpAddress': '13.233.149.161',
			'State': {
				'Code': 16,
				'Name': 'running'
			},
			'StateTransitionReason': '',
			'SubnetId': 'subnet-763c651f',
			'VpcId': 'vpc-b680d3df',
			'Architecture': 'x86_64',
			'IamInstanceProfile': {
				'Arn': 'arn:aws:iam::082923708139:instance-profile/EC2-AWS-CICD-Roile',
				'Id': 'AIPARGTVDL3VW3O4VSDK6'
			},
			'NetworkInterfaces': [{
				'Association': {
					'IpOwnerId': 'amazon',
					'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
					'PublicIp': '13.233.149.161'
				},
				'Attachment': {
					'AttachTime': datetime.datetime(2020, 12, 5, 4, 24, 7, tzinfo = tzlocal()),
					'AttachmentId': 'eni-attach-08cfd5390b05b478a',
					'DeleteOnTermination': True,
					'DeviceIndex': 0,
					'Status': 'attached'
				},
				'Description': '',
				'Groups': [{
					'GroupName': 'launch-wizard-2',
					'GroupId': 'sg-068aab378fd4baf27'
				}],
				'Ipv6Addresses': [],
				'MacAddress': '02:ce:d0:5a:79:d0',
				'NetworkInterfaceId': 'eni-0d047c9183d815761',
				'OwnerId': '082923708139',
				'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
				'PrivateIpAddress': '172.31.29.10',
				'PrivateIpAddresses': [{
					'Association': {
						'IpOwnerId': 'amazon',
						'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
						'PublicIp': '13.233.149.161'
					},
					'Primary': True,
					'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
					'PrivateIpAddress': '172.31.29.10'
				}],
				'SourceDestCheck': True,
				'Status': 'in-use',
				'SubnetId': 'subnet-763c651f',
				'VpcId': 'vpc-b680d3df',
				'InterfaceType': 'interface'
			}],
			'RootDeviceName': '/dev/xvda',
			'RootDeviceType': 'ebs',
			'SecurityGroups': [{
				'GroupName': 'launch-wizard-2',
				'GroupId': 'sg-068aab378fd4baf27'
			}],
			'SourceDestCheck': True,
			'Tags': [{
				'Key': 'Name',
				'Value': 'EC2-A'
			}],
			'VirtualizationType': 'hvm',
			'CpuOptions': {
				'CoreCount': 1,
				'ThreadsPerCore': 1
			},
			'CapacityReservationSpecification': {
				'CapacityReservationPreference': 'open'
			},
			'HibernationOptions': {
				'Configured': False
			},
			'MetadataOptions': {
				'State': 'applied',
				'HttpTokens': 'optional',
				'HttpPutResponseHopLimit': 1,
				'HttpEndpoint': 'enabled'
			},
			'EnclaveOptions': {
				'Enabled': False
			}
		}],
		'OwnerId': '082923708139',
		'ReservationId': 'r-00b4fb251f781e276'
	}],
	'ResponseMetadata': {
		'RequestId': '1d003b2f-5fad-4e8c-ada7-e7ca2a33fb1d',
		'HTTPStatusCode': 200,
		'HTTPHeaders': {
			'x-amzn-requestid': '1d003b2f-5fad-4e8c-ada7-e7ca2a33fb1d',
			'content-type': 'text/xml;charset=UTF-8',
			'transfer-encoding': 'chunked',
			'vary': 'accept-encoding',
			'date': 'Sun, 13 Dec 2020 05:52:52 GMT',
			'server': 'AmazonEC2'
		},
		'RetryAttempts': 0
	}
}

'''
