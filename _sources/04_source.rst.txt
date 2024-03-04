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

.. http:get:: /api/user/list
   :noindex:
   
     Get followers
	 
   :>json json followers: List of followers

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
         "extra": {
            "fatal_item_ids": [],
            "logid": "20231204180523B9C3034B5CF8695EBE51",
            "now": 1701713124000
         },
         "hasMore": true,
         "log_pb": {
            "impr_id": "20231204180523B9C3034B5CF8695EBE51"
         },
         "maxCursor": 1701698692,
         "minCursor": 1701685519,
         "statusCode": 0,
         "status_code": 0,
         "total": 518808,
         "userList": [
            {
                  "stats": {
                     "diggCount": 11600,
                     "followerCount": 224,
                     "followingCount": 3215,
                     "friendCount": 0,
                     "heart": 272,
                     "heartCount": 272,
                     "videoCount": 29
                  },
                  "user": {
                     "avatarLarger": <string>,
                     "avatarMedium": <string>,
                     "avatarThumb": <string>,
                     "commentSetting": 1,
                     "downloadSetting": 3,
                     "duetSetting": 3,
                     "ftc": false,
                     "id": "7277635517649699845",
                     "isADVirtual": false,
                     "nickname": <string>,
                     "openFavorite": false,
                     "privateAccount": false,
                     "relation": 0,
                     "secUid": <string>,
                     "secret": false,
                     "signature": <string>,
                     "stitchSetting": 3,
                     "ttSeller": false,
                     "uniqueId": <string>,
                     "verified": false
                  }
            },
         ]
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


.. http:get:: /api/explore/item_list
   :noindex:
   
     Get trending videos
	 
   :>json json videos: List of videos

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript
      
      {
         "BAInfo": "",
         "adAuthorization": false,
         "adLabelVersion": 0,
         "author": {
               "avatarLarger": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/ba1e7df48c5a3682582da7989016fc16~c5_1080x1080.jpeg?x-expires=1701882000\u0026x-signature=DnP7GG6IbQJPGJBieDMWOcdUUA0%3D",
               "avatarMedium": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/ba1e7df48c5a3682582da7989016fc16~c5_720x720.jpeg?x-expires=1701882000\u0026x-signature=tarGE0dyTybP7InrBusGH7F6TfA%3D",
               "avatarThumb": "https://p16-sign-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/ba1e7df48c5a3682582da7989016fc16~c5_100x100.jpeg?x-expires=1701882000\u0026x-signature=%2BPWCEbAB9WW8YmsbbTb%2FKh5byUA%3D",
               "commentSetting": 0,
               "downloadSetting": 3,
               "duetSetting": 3,
               "ftc": false,
               "id": "6780231953461478401",
               "isADVirtual": false,
               "isEmbedBanned": false,
               "nickname": "Fitria Marala",
               "openFavorite": false,
               "privateAccount": false,
               "relation": 0,
               "secUid": "MS4wLjABAAAAFdBt489FnKNr0IrpsKhY_zFiLcvB7X9E9XHdwdkOr7JEfurVxcXu4bQ3AnYh2HJ9",
               "secret": false,
               "signature": <string>,
               "stitchSetting": 3,
               "ttSeller": true,
               "uniqueId": "_fitr13",
               "verified": false
         },
         "authorStats": {
               "diggCount": 35400,
               "followerCount": 19000,
               "followingCount": 72,
               "friendCount": 0,
               "heart": 4000000,
               "heartCount": 4000000,
               "videoCount": 14
         },
         "collected": false,
         "contents": [
               {
                  "desc": <string>
               }
         ],
         "createTime": 1701169484,
         "desc": <string>,
         "digged": false,
         "diversificationId": 10066,
         "duetDisplay": 0,
         "duetEnabled": false,
         "duetInfo": {
               "duetFromId": "0"
         },
         "forFriend": false,
         "id": <string>,
         "isAd": false,
         "itemCommentStatus": 0,
         "itemMute": false,
         "music": {
               "album": "",
               "authorName": "question mark",
               "coverLarge": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~c5_1080x1080.jpeg?x-expires=1701882000\u0026x-signature=dm%2FI9r5oLOEtpcLRjA4Zx42XbCk%3D",
               "coverMedium": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~c5_720x720.jpeg?x-expires=1701882000\u0026x-signature=w99ww%2BBRGG6Zg9KPvByT5MmKxAc%3D",
               "coverThumb": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~c5_100x100.jpeg?x-expires=1701882000\u0026x-signature=u%2FkeM1JKCKsSA9LpkeuHPO6R3Js%3D",
               "duration": 42,
               "id": "7279680270842874630",
               "original": true,
               "playUrl": "https://v77.tiktokcdn.com/3eb253b9646ebc0ff533f425b96746f6/656e2134/video/tos/useast2a/tos-useast2a-v-27dcd7/ocABJQlYnve6pBPBQDbVCPUyf87j2lBUkWOJnN/?a=1233\u0026ch=0\u0026cr=0\u0026dr=0\u0026er=2\u0026cd=0%7C0%7C0%7C0\u0026br=250\u0026bt=125\u0026bti=NDU3ZjAwOg%3D%3D\u0026ft=d2A~l-Inz7TS152Ziyq8Z\u0026mime_type=audio_mpeg\u0026qs=6\u0026rc=NmY2NmRoNzpkaDdnZTk4ZEBpajNpaDg6Zjw8bjMzNzU8M0BeXjMxMzIzXzUxYi8zMTAtYSNnczRrcjRfcTBgLS1kMTZzcw%3D%3D\u0026l=2023120417571317E0A4084BE6C75B3246\u0026btag=e00088000\u0026cc=13\u0026download=true",
               "title": "original sound - question mark"
         },
         "officalItem": false,
         "originalItem": false,
         "playlistId": "",
         "privateItem": false,
         "secret": false,
         "shareEnabled": true,
         "showNotPass": false,
         "stats": {
               "collectCount": 362000,
               "commentCount": 9062,
               "diggCount": 4000000,
               "playCount": 20000000,
               "shareCount": 79700
         },
         "stitchDisplay": 0,
         "stitchEnabled": false,
         "video": {
               "bitrate": 1451746,
               "bitrateInfo": [
                  {
                     "Bitrate": 1561318,
                     "CodecType": "h265_hvc1",
                     "GearName": "adapt_lowest_1080_1",
                     "PlayAddr": {
                           "DataSize": 2036350,
                           "FileCs": "c:0-10305-7bc0",
                           "FileHash": "d1d995c95debfa4c38f1bb69a9d96f27",
                           "Uri": "v14044g50000clisifnog65grp6351j0",
                           "UrlKey": "v14044g50000clisifnog65grp6351j0_bytevc1_1080p_1561318",
                           "UrlList": [
                              <string>
                           ]
                     },
                     "QualityType": 2
                  },
                  {
                     "Bitrate": 1451746,
                     "CodecType": "h264",
                     "GearName": "normal_540_0",
                     "PlayAddr": {
                           "DataSize": 1893440,
                           "FileCs": "c:0-10159-d9dc",
                           "FileHash": "33c9de442d59cc9c1d5d4e104b69d827",
                           "Uri": "v14044g50000clisifnog65grp6351j0",
                           "UrlKey": "v14044g50000clisifnog65grp6351j0_h264_540p_1451746",
                           "UrlList": [
                              <string>
                           ]
                     },
                     "QualityType": 20
                  },
                  {
                     "Bitrate": 906902,
                     "CodecType": "h265_hvc1",
                     "GearName": "adapt_lower_720_1",
                     "PlayAddr": {
                           "DataSize": 1182828,
                           "FileCs": "c:0-10306-4a4a",
                           "FileHash": "f089fc3f5761f8e9e683dc54b80bd7b9",
                           "Uri": "v14044g50000clisifnog65grp6351j0",
                           "UrlKey": "v14044g50000clisifnog65grp6351j0_bytevc1_720p_906902",
                           "UrlList": [
                              <string>
                           ]
                     },
                     "QualityType": 14
                  },
                  {
                     "Bitrate": 712302,
                     "CodecType": "h264",
                     "GearName": "lower_540_0",
                     "PlayAddr": {
                           "DataSize": 929021,
                           "FileCs": "c:0-10159-c9d1",
                           "FileHash": "4a7f1e76fd2a60c061c81878016d62ee",
                           "Uri": "v14044g50000clisifnog65grp6351j0",
                           "UrlKey": "v14044g50000clisifnog65grp6351j0_h264_540p_712302",
                           "UrlList": [
                              <string>
                           ]
                     },
                     "QualityType": 24
                  },
                  {
                     "Bitrate": 690608,
                     "CodecType": "h265_hvc1",
                     "GearName": "adapt_540_1",
                     "PlayAddr": {
                           "DataSize": 900726,
                           "FileCs": "c:0-10306-ddd9",
                           "FileHash": "c15cf5fe0f9c593136fded088dd4e1df",
                           "Uri": "v14044g50000clisifnog65grp6351j0",
                           "UrlKey": "v14044g50000clisifnog65grp6351j0_bytevc1_540p_690608",
                           "UrlList": [
                              <string>
                           ]
                     },
                     "QualityType": 28
                  }
               ],
               "codecType": "h264",
               "cover": "https://p16-sign-sg.tiktokcdn.com/obj/tos-alisg-p-0037/oYPZDYXcplJVOVB3iiBvWIEMwwyk3yBBhAEmA?x-expires=1701882000\u0026x-signature=DiF3PvAeSJKONwiKFMthqOAP85I%3D",
               "definition": "540p",
               "downloadAddr": <string>,
               "duration": 10,
               "dynamicCover": "https://p16-sign-sg.tiktokcdn.com/obj/tos-alisg-p-0037/5e7ee1e9e9384552ae3775f49db46801_1701169488?x-expires=1701882000\u0026x-signature=70l%2BXQk1iARzH7dptObbcQWMfVQ%3D",
               "encodeUserTag": "",
               "encodedType": "normal",
               "format": "mp4",
               "height": 1024,
               "id": "7306467281624747282",
               "originCover": "https://p16-sign-sg.tiktokcdn.com/obj/tos-alisg-p-0037/65663301006047c4b8a174aff56a6f84_1701169486?x-expires=1701882000\u0026x-signature=EjnH8NuoBpLFu0jVuzFP5tVm12A%3D",
               "playAddr": <string>,
               "ratio": "540p",
               "reflowCover": <string>,
               "shareCover": [
                  "",
                  <string>
               ],
               "size": 1893440,
               "videoQuality": "normal",
               "volumeInfo": {
                  "Loudness": -19.9,
                  "Peak": 0.41687
               },
               "width": 576,
               "zoomCover": {
                  "240": <string>,
                  "480": <string>,
                  "720": <string>,
                  "960": <string>
               }
         },
         "vl1": false
      }