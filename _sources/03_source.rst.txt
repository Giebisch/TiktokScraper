Source Data
===========

In this section a collection of all the API calls the Tiktok Web App makes will be listed.
This is the raw data from the Tiktok backend, not from the scraper itself.

.. http:get:: /
   :noindex:
   
     Query Parameters necessary for all types of request
	 
   :query string:  WebIdLastTime (*required*) -- 
   :query string:  aid (*required*) -- 
   :query string:  app_lanugage (*required*) -- 
   :query string:  app_name (*required*) -- 
   :query string:  aweme_id (*required*) -- 
   :query string:  browser_language (*required*) -- 
   :query string:  browser_name (*required*) -- 
   :query string:  browser_platform (*required*) -- 
   :query string:  browser_version (*required*) -- 
   :query string:  channel (*required*) -- 
   :query string:  cookie_enabled (*required*) -- 
   :query string:  count (*required*) -- 
   :query string:  current_region (*required*) -- 
   :query string:  cursor (*required*) -- 
   :query string:  device_id (*required*) -- 
   :query string:  device_platform (*required*) -- 
   :query string:  enter_from (*required*) -- 
   :query string:  focus_state (*required*) -- 
   :query string:  fromWeb (*required*) -- 
   :query string:  from_page (*required*) -- 
   :query string:  history_len (*required*) -- 
   :query string:  is_fullscreen (*required*) -- 
   :query string:  is_non_personalized (*required*) -- 
   :query string:  is_page_visible (*required*) -- 
   :query string:  os (*required*) -- 
   :query string:  priority_region (*required*) -- 
   :query string:  referer (*required*) -- 
   :query string:  region (*required*) -- 
   :query string:  screen_height (*required*) -- 
   :query string:  screen_width (*required*) -- 
   :query string:  tz_name (*required*) -- 
   :query string:  webcast_language (*required*) -- 
   :query string:  msToken (*required*) -- 
   :query string:  _signature (*required*) -- 
   
   :requestheader Authorization: `msToken`
   :requestheader Cookie: token from response of last request `X-Ms-Token`
   
.. important::
   It seems like all (or at least most) of the query parameters are necessary

.. http:get:: /api/user/detail/
   :noindex:
   
     Get details of user
	 
   :>json json userInfo: userInfo

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "userInfo": {
            "stats": {
                  "diggCount": 0,
                  "followerCount": 869400,
                  "followingCount": 15,
                  "friendCount": 5,
                  "heart": 14900000,
                  "heartCount": 14900000,
                  "videoCount": 189
            },
            "user": {
                  "avatarLarger": <link>,
                  "avatarMedium": <link>,
                  "avatarThumb": <link>,
                  "canExpPlaylist": true,
                  "commentSetting": 0,
                  "commerceUserInfo": {
                     "commerceUser": false
                  },
                  "duetSetting": 0,
                  "followingVisibility": 1,
                  "ftc": false,
                  "id": <string id>,
                  "isADVirtual": false,
                  "isEmbedBanned": false,
                  "nickNameModifyTime": 1659513420,
                  "nickname": <string>,
                  "openFavorite": false,
                  "privateAccount": false,
                  "profileEmbedPermission": 1,
                  "profileTab": {
                     "showPlayListTab": false,
                     "showQuestionTab": true
                  },
                  "relation": 0,
                  "secUid": <string>,
                  "secret": false,
                  "signature": <string>,
                  "stitchSetting": 0,
                  "ttSeller": false,
                  "uniqueId": <string>,
                  "verified": false
            }
         }
      }

.. http:get:: /api/comment/list
   :noindex:
   
     Get comments of a video
	 
   :>json json comments: List of comments

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
      "alias_comment_deleted": false,
      "comments": [
         {
               "author_pin": false,
               "aweme_id": "7279848477109062945",
               "cid": "7280136767352308512",
               "collect_stat": 0,
               "comment_language": "de",
               "create_time": 1695038967,
               "digg_count": 1413,
               "image_list": null,
               "is_author_digged": true,
               "label_list": [
                  {
                     "text": <string>,
                     "type": 20
                  }
               ],
               "no_show": false,
               "reply_comment": [
                  {
                     "aweme_id": "7279848477109062945",
                     "cid": "7280143271883981600",
                     "collect_stat": 0,
                     "comment_language": "de",
                     "create_time": 1695040498,
                     "digg_count": 392,
                     "image_list": null,
                     "is_author_digged": false,
                     "label_list": [
                           {
                              "text": <string>,
                              "type": 1
                           }
                     ],
                     "label_text": <string>,
                     "label_type": 1,
                     "no_show": false,
                     "reply_comment": null,
                     "reply_id": "7280136767352308512",
                     "reply_to_reply_id": "0",
                     "share_info": {
                           "acl": {
                              "code": 1,
                              "extra": "{\"item_share_acl\":\"empty item value\"}"
                           },
                           "desc": <string>,
                           "title": <string>,
                           "url": <string>,
                     },
                     "status": 1,
                     "text": <string>,
                     "text_extra": [],
                     "trans_btn_style": 1,
                     "user": {
                           "account_labels": null,
                           "ad_cover_url": null,
                           "advance_feature_item_order": null,
                           "advanced_feature_info": null,
                           "avatar_thumb": {
                              "uri": "tos-useast2a-avt-0068-euttp/d106515243ceb865bacd4db68ea94283",
                              "url_list": [
                                 <string>
                              ],
                              "url_prefix": null
                           },
                           "bold_fields": null,
                           "can_message_follow_status_list": null,
                           "can_set_geofencing": null,
                           "cha_list": null,
                           "cover_url": null,
                           "custom_verify": "",
                           "enterprise_verify_reason": "",
                           "events": null,
                           "followers_detail": null,
                           "geofencing": null,
                           "homepage_bottom_toast": null,
                           "item_list": null,
                           "mutual_relation_avatars": null,
                           "need_points": null,
                           "nickname": <string>,
                           "platform_sync_info": null,
                           "relative_users": null,
                           "search_highlight": null,
                           "sec_uid": <string>,
                           "shield_edit_field_info": null,
                           "type_label": null,
                           "uid": "6958026025243706373",
                           "unique_id": <string>,
                           "user_profile_guide": null,
                           "user_tags": null,
                           "white_cover_url": null
                     },
                     "user_buried": false,
                     "user_digged": 0
                  }
               ],
               "reply_comment_total": 8,
               "reply_id": "0",
               "reply_to_reply_id": "0",
               "share_info": {
                  "acl": {
                     "code": 1,
                     "extra": "{\"item_share_acl\":\"empty item value\"}"
                  },
                  "desc": <string>,
                  "title": <string>,
                  "url": <string>
               },
               "status": 1,
               "stick_position": 0,
               "text": <string>,
               "text_extra": [],
               "trans_btn_style": 1,
               "user": {
                  "account_labels": null,
                  "ad_cover_url": null,
                  "advance_feature_item_order": null,
                  "advanced_feature_info": null,
                  "avatar_thumb": {
                     "uri": "tos-useast2a-avt-0068-euttp/d8b118380e3ddbd227adf3c20042e5a9",
                     "url_list": [
                           <string>
                     ],
                     "url_prefix": null
                  },
                  "bold_fields": null,
                  "can_message_follow_status_list": null,
                  "can_set_geofencing": null,
                  "cha_list": null,
                  "cover_url": null,
                  "custom_verify": "",
                  "enterprise_verify_reason": "",
                  "events": null,
                  "followers_detail": null,
                  "geofencing": null,
                  "homepage_bottom_toast": null,
                  "item_list": null,
                  "mutual_relation_avatars": null,
                  "need_points": null,
                  "nickname": "vykdzgdrn47",
                  "platform_sync_info": null,
                  "relative_users": null,
                  "search_highlight": null,
                  "sec_uid": "MS4wLjABAAAA5SL64ddtcxtnLNxRWIeq427MNy1BSnxaEcbxQPaXtEzUwMVfKHY6m8Pzpsq8yG9A",
                  "shield_edit_field_info": null,
                  "type_label": null,
                  "uid": "7275216108189271073",
                  "unique_id": "vykdzwcwk",
                  "user_profile_guide": null,
                  "user_tags": null,
                  "white_cover_url": null
               },
               "user_buried": false,
               "user_digged": 0
         },
      }
