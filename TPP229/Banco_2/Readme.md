# Readme file for TPP229 

## Client Details 
 clientID=18c07b85-3016-4dbf-974e-215e549269ac 
 clientSecret=ce128ceb-ea0b-4cc7-9227-d6f36b19bc19 

## Organisation Details 
 orgName=TPP229 
 orgID=1e907ed7-8e85-4e6a-9974-03e9814d923d 

## Software Details 
 softwareName=TPP229 
 softwareID=405124f7-e042-4f12-bdaf-a3305d17a41b 

## Cert KID Details 
 transportKID=h3e67shr9r7wroD1aIysvk-nEXs8Qu-lCRgl2TqDVks 
 signingKID=6IUg1uQsxwmAyqbeX-bCbh4NUASj2NHxBU4HBH1BzBs 

## Cert Pem Details 
 transportPEM=https://tecban-uat-us-east-1-keystore.s3.amazonaws.com/1e907ed7-8e85-4e6a-9974-03e9814d923d/405124f7-e042-4f12-bdaf-a3305d17a41b/h3e67shr9r7wroD1aIysvk-nEXs8Qu-lCRgl2TqDVks.pem 
 signingPEM=https://tecban-uat-us-east-1-keystore.s3.amazonaws.com/1e907ed7-8e85-4e6a-9974-03e9814d923d/405124f7-e042-4f12-bdaf-a3305d17a41b/6IUg1uQsxwmAyqbeX-bCbh4NUASj2NHxBU4HBH1BzBs.pem 

## Server Details 
 Well Known Endpoint=https://auth2.tecban-sandbox.o3bank.co.uk/.well-known/openid-configuration 
 Token Endpoint=https://as2.tecban-sandbox.o3bank.co.uk/token 
 Resource Endpoint=https://rs2.tecban-sandbox.o3bank.co.uk 
 Auth Endpoint=https://auth2.tecban-sandbox.o3bank.co.uk/auth 

 ## User & Account Details 
 [
  {
    "username": "team229b2u1",
    "password": "337975",
    "accounts": [
      {
        "accountNumber": "02229001001"
      },
      {
        "accountNumber": "02229001002"
      },
      {
        "accountNumber": "02229001003"
      }
    ]
  },
  {
    "username": "team229b2u2",
    "password": "733019",
    "accounts": [
      {
        "accountNumber": "02229002001"
      },
      {
        "accountNumber": "02229002002"
      },
      {
        "accountNumber": "02229002003"
      }
    ]
  },
  {
    "username": "team229b2u3",
    "password": "779926",
    "accounts": [
      {
        "accountNumber": "02229003001"
      },
      {
        "accountNumber": "02229003002"
      },
      {
        "accountNumber": "02229003003"
      }
    ]
  },
  {
    "username": "team229b2u4",
    "password": "675690",
    "accounts": [
      {
        "accountNumber": "02229004001"
      },
      {
        "accountNumber": "02229004002"
      },
      {
        "accountNumber": "02229004003"
      }
    ]
  },
  {
    "username": "team229b2u5",
    "password": "737934",
    "accounts": [
      {
        "accountNumber": "02229005001"
      },
      {
        "accountNumber": "02229005002"
      },
      {
        "accountNumber": "02229005003"
      }
    ]
  }
] 

## Tip for testing in postman 
 In postman settings - certificates tab - add the transport cert and key for the rs and token endpoints 

