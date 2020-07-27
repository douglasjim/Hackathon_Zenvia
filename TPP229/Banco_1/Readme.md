# Readme file for TPP229 

## Client Details 
 clientID=fdbb1d98-1b30-41b7-9605-728e76a7d3d6 
 clientSecret=b10dfe3e-247d-4a01-a8c1-185ba4f4ea93 

## Organisation Details 
 orgName=TPP229 
 orgID=a5616d9d-6246-40c6-ab33-8afefc54dbc6 

## Software Details 
 softwareName=TPP229 
 softwareID=159d5d5b-cd88-491e-ba40-0747be4c4cf7 

## Cert KID Details 
 transportKID=dpKYc9eXv71Fwa5eAkLaU5ZSdTE8nUReMATaoMBEQQE 
 signingKID=w2LY1p2PIOzEqcB7qoyHO4Xw2A1W0o2wEEOJswu4ifU 

## Cert Pem Details 
 transportPEM=https://tecban-uat-us-east-1-keystore.s3.amazonaws.com/a5616d9d-6246-40c6-ab33-8afefc54dbc6/159d5d5b-cd88-491e-ba40-0747be4c4cf7/dpKYc9eXv71Fwa5eAkLaU5ZSdTE8nUReMATaoMBEQQE.pem 
 signingPEM=https://tecban-uat-us-east-1-keystore.s3.amazonaws.com/a5616d9d-6246-40c6-ab33-8afefc54dbc6/159d5d5b-cd88-491e-ba40-0747be4c4cf7/w2LY1p2PIOzEqcB7qoyHO4Xw2A1W0o2wEEOJswu4ifU.pem 

## Server Details 
 Well Known Endpoint=https://auth1.tecban-sandbox.o3bank.co.uk/.well-known/openid-configuration 
 Token Endpoint=https://as1.tecban-sandbox.o3bank.co.uk/token 
 Resource Endpoint=https://rs1.tecban-sandbox.o3bank.co.uk 
 Auth Endpoint=https://auth1.tecban-sandbox.o3bank.co.uk/auth 

 ## User & Account Details 
 [
  {
    "username": "team229b1u1",
    "password": "453331",
    "accounts": [
      {
        "accountNumber": "01229001001"
      },
      {
        "accountNumber": "01229001002"
      },
      {
        "accountNumber": "01229001003"
      }
    ]
  },
  {
    "username": "team229b1u2",
    "password": "723635",
    "accounts": [
      {
        "accountNumber": "01229002001"
      },
      {
        "accountNumber": "01229002002"
      },
      {
        "accountNumber": "01229002003"
      }
    ]
  },
  {
    "username": "team229b1u3",
    "password": "408473",
    "accounts": [
      {
        "accountNumber": "01229003001"
      },
      {
        "accountNumber": "01229003002"
      },
      {
        "accountNumber": "01229003003"
      }
    ]
  },
  {
    "username": "team229b1u4",
    "password": "803119",
    "accounts": [
      {
        "accountNumber": "01229004001"
      },
      {
        "accountNumber": "01229004002"
      },
      {
        "accountNumber": "01229004003"
      }
    ]
  },
  {
    "username": "team229b1u5",
    "password": "737036",
    "accounts": [
      {
        "accountNumber": "01229005001"
      },
      {
        "accountNumber": "01229005002"
      },
      {
        "accountNumber": "01229005003"
      }
    ]
  }
] 

## Tip for testing in postman 
 In postman settings - certificates tab - add the transport cert and key for the rs and token endpoints 

