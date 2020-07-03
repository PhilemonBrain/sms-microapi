from .views import sendmessage, translateMessages, nuobj_api, TwilioSendSms, GroupList, GroupBySenderList, GroupDetail, GroupCreate, GroupNumbersList,GroupNumbersCreate, GroupNumbersDetail, SmsHistoryList, SmsHistoryDetail, send_group_twilio #sendmessage_infobip, get_recipients_ibp
from django.urls import path
from .views import create_receipents_details, save_recipients_details, sms_list  #get_recipient_details
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

#doc_view = get_swagger_view(title="SMS API documentation") #This generator is no longer used
schema_view = get_schema_view(
   openapi.Info(
      title="SMS API",
      default_version='v1',
      description="""SMS API testing - This is done using PostMan Testing tool. To start, you need to register using the '/v1/register endpoint'. Using a key-value instance, 
        post your email, phoneNumber, name, password with the former as the respective keys, also specify content-type and make sure it is set to application/json.
        Set the HTTP Method to post and hit send. Your account has been created. Next is to get your token via 'v1/api-token-auth/' endpoint using the key-value instance 
        of username and password (username being your email address). Copy the given token. To test any endpoint, you need to add your token to the header tab using key-value. 
        in the format {"Authorization": "Token <your token you copied>"}. LET'S TEST!!!.
      """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/sms/recipient/create', create_receipents_details),
    path('v1/sms/recipient/save', save_recipients_details),
    #path('v1/sms/recipient/all', get_recipient_details),
    path('v1/sms/message/translate', translateMessages),
    path('v1/sms/twilio_send_group', send_group_twilio),
    #path('swagger(P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'), #not used for now
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/sms/twillo_sms_history', sms_list),
    path('v1/sms/sms_history/<senderID>', SmsHistoryList.as_view(), name="history"),
    path('v1/sms/sms_history/<str:pk>', SmsHistoryDetail.as_view(), name="history_"),
    path('v1/sms/twilio_send_single', TwilioSendSms.as_view(), name="sendsms"),
    # infobip view
    # path('v1/sms/infobip/send', sendmessage_infobip),
    # path('v1/sms/infobip/reports', get_recipients_ibp),
    path('v1/sms/nuobjects/send',nuobj_api),
    path("v1/sms/list_group", GroupList.as_view(), name="list-group"),
    path("v1/sms/list_group/<senderID>", GroupBySenderList.as_view(), name="list-group"),
    path("v1/sms/create_group", GroupCreate.as_view(), name="update-group"),
    path("v1/sms/group_update/<str:pk>", GroupDetail.as_view(), name="update-group"),
    path("v1/sms/group_recipient/", GroupNumbersList.as_view(), name="group-numbers"),
    path("v1/sms/group_recipient/create", GroupNumbersCreate.as_view(), name="create-group-numbers"),
    path("v1/sms/group_number/<senderID>", GroupNumbersDetail.as_view(), name="update-group-umbers"),
   #  swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include_docs_urls(title='SMS API', description=
    """
        SMS API testing - This is done using PostMan Testing tool. To start, all you need to do is have a senderID or userID. Once supplied, it would be used to 
        identify all transactions done by you. To send a single sms using an service,visit the respective endpoint and follow the instructions based on format and 
        request to be sent. Remember senderID == userID, and this is personally generated. LET'S TEST!!!."""
    ,permission_classes=(permissions.AllowAny,)))
]

