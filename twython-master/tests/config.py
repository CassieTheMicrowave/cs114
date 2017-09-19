import os

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    import unittest2 as unittest
else:
    import unittest

app_key = os.environ.get('APP_KEY')
app_secret = os.environ.get('APP_SECRET')
oauth_token = os.environ.get('OAUTH_TOKEN')
oauth_token_secret = os.environ.get('OAUTH_TOKEN_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')

screen_name = os.environ.get('SCREEN_NAME', '__twython__')

# Protected Account you ARE following and they ARE following you
protected_twitter_1 = os.environ.get('PROTECTED_TWITTER_1', 'TwythonSecure1')

# Protected Account you ARE NOT following
protected_twitter_2 = os.environ.get('PROTECTED_TWITTER_2', 'TwythonSecure2')

# Test Ids
test_tweet_id = os.environ.get('TEST_TWEET_ID', '318577428610031617')
test_list_slug = os.environ.get('TEST_LIST_SLUG', 'team')
test_list_owner_screen_name = os.environ.get('TEST_LIST_OWNER_SCREEN_NAME',
                                             'twitterapi')

test_tweet_object = {u'contributors': None, u'truncated': False, u'text': u'http://t.co/FCmXyI6VHd is a #cool site, lol! @mikehelmick shd #checkitout. Love, @__twython__ https://t.co/67pwRvY6z9 http://t.co/N6InAO4B71', u'in_reply_to_status_id': None, u'id': 349683012054683648, u'favorite_count': 0, u'source': u'web', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [{u'id': 29251354, u'indices': [45, 57], u'id_str': u'29251354', u'screen_name': u'mikehelmick', u'name': u'Mike Helmick'}, {u'id': 1431865928, u'indices': [81, 93], u'id_str': u'1431865928', u'screen_name': u'__twython__', u'name': u'Twython'}], u'hashtags': [{u'indices': [28, 33], u'text': u'cool'}, {u'indices': [62, 73], u'text': u'checkitout'}], u'urls': [{u'url': u'http://t.co/FCmXyI6VHd', u'indices': [0, 22], u'expanded_url': u'http://google.com', u'display_url': u'google.com'}, {u'url': u'https://t.co/67pwRvY6z9', u'indices': [94, 117], u'expanded_url': u'https://github.com', u'display_url': u'github.com'}], u'media': [{u'id': 537884378513162240, u'id_str': u'537884378513162240', u'indices': [118, 140], u'media_url': u'http://pbs.twimg.com/media/B3by_g-CQAAhrO5.jpg', u'media_url_https': u'https://pbs.twimg.com/media/B3by_g-CQAAhrO5.jpg', u'url': u'http://t.co/N6InAO4B71', u'display_url': u'pic.twitter.com/N6InAO4B71', u'expanded_url': u'http://twitter.com/pingofglitch/status/537884380060844032/photo/1', u'type': u'photo', u'sizes': {u'large': {u'w': 1024, u'h': 640, u'resize': u'fit'}, u'thumb': {u'w': 150, u'h': 150, u'resize': u'crop'}, u'medium': {u'w': 600, u'h': 375, u'resize': u'fit'}, u'small': {u'w': 340, u'h': 212, u'resize': u'fit'}}}]}, u'in_reply_to_screen_name': None, u'id_str': u'349683012054683648', u'retweet_count': 0, u'in_reply_to_user_id': None, u'favorited': False, u'user': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': True, u'id': 1431865928, u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://si0.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'description': {u'urls': []}}, u'followers_count': 1, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'1431865928', u'profile_background_color': u'3D3D3D', u'listed_count': 0, u'profile_background_image_url_https': u'https://si0.twimg.com/images/themes/theme1/bg.png', u'utc_offset': None, u'statuses_count': 2, u'description': u'', u'friends_count': 1, u'location': u'', u'profile_link_color': u'0084B4', u'profile_image_url': u'http://a0.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://a0.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'__twython__', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 0, u'name': u'Twython', u'notifications': False, u'url': None, u'created_at': u'Thu May 16 01:11:09 +0000 2013', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'lang': u'en', u'created_at': u'Wed Jun 26 00:18:21 +0000 2013', u'in_reply_to_status_id_str': None, u'place': None}
test_tweet_html = '<a href="http://t.co/FCmXyI6VHd" class="twython-url">google.com</a> is a <a href="https://twitter.com/search?q=%23cool" class="twython-hashtag">#cool</a> site, lol! <a href="https://twitter.com/mikehelmick" class="twython-mention">@mikehelmick</a> shd <a href="https://twitter.com/search?q=%23checkitout" class="twython-hashtag">#checkitout</a>. Love, <a href="https://twitter.com/__twython__" class="twython-mention">@__twython__</a> <a href="https://t.co/67pwRvY6z9" class="twython-url">github.com</a> <a href="http://t.co/N6InAO4B71" class="twython-media">pic.twitter.com/N6InAO4B71</a>'

test_tweet_symbols_object = {u'text': u'Some symbols: $AAPL and $PEP and $ANOTHER and $A.', u'contributors': None, u'geo': None, u'favorited': True, u'in_reply_to_user_id_str': None, u'user': {u'location': u'', u'id_str': u'2030131', u'protected': False, u'profile_background_tile': False, u'friends_count': 18, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'entities': {u'description': {u'urls': []}}, u'lang': u'en', u'listed_count': 5, u'default_profile_image': True, u'default_profile': False, u'statuses_count': 447, u'notifications': False, u'profile_background_color': u'9AE4E8', u'profile_sidebar_fill_color': u'E0FF92', u'profile_link_color': u'0000FF', u'profile_image_url_https': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_5_normal.png', u'followers_count': 8, u'geo_enabled': True, u'following': True, u'has_extended_profile': False, u'profile_use_background_image': True, u'profile_text_color': u'000000', u'screen_name': u'philgyfordtest', u'contributors_enabled': False, u'verified': False, u'name': u'Phil Gyford Test', u'profile_sidebar_border_color': u'000000', u'utc_offset': 0, u'profile_image_url': u'http://abs.twimg.com/sticky/default_profile_images/default_profile_5_normal.png', u'id': 2030131, u'favourites_count': 0, u'time_zone': u'London', u'url': None, u'is_translation_enabled': False, u'is_translator': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'description': u'', u'created_at': u'Fri Mar 23 16:56:52 +0000 2007', u'follow_request_sent': False}, u'in_reply_to_user_id': None, u'retweeted': False, u'coordinates': None, u'place': None, u'in_reply_to_status_id': None, u'lang': u'en', u'in_reply_to_status_id_str': None, u'truncated': False, u'retweet_count': 0, u'is_quote_status': False, u'id': 662694880657989632, u'id_str': u'662694880657989632', u'in_reply_to_screen_name': None, u'favorite_count': 1, u'entities': {u'hashtags': [], u'user_mentions': [], u'symbols': [{u'indices': [14, 19], u'text': u'AAPL'}, {u'indices': [24, 28], u'text': u'PEP'}, {u'indices': [46, 48], u'text': u'A'}], u'urls': []}, u'created_at': u'Fri Nov 06 18:15:46 +0000 2015', u'source': u'<a href="http://tapbots.com/software/tweetbot/mac" rel="nofollow">Tweetbot for Mac</a>'}

test_tweet_compat_object = {u'contributors': None, u'truncated': True, u'text': u"Say more about what's happening! Rolling out now: photos, videos, GIFs, polls, and Quote Tweets no longer count tow\u2026 https://t.co/SRmsuks2ru", u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 777915304261193728, u'favorite_count': 13856, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [{u'url': u'https://t.co/SRmsuks2ru', u'indices': [117, 140], u'expanded_url': u'https://twitter.com/i/web/status/777915304261193728', u'display_url': u'twitter.com/i/web/status/7\u2026'}]}, u'in_reply_to_screen_name': None, u'id_str': u'777915304261193728', u'retweet_count': 14767, u'in_reply_to_user_id': None, u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'id': 783214, u'verified': True, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/767879603977191425/29zfZY6I_normal.jpg', u'profile_sidebar_fill_color': u'F6F6F6', u'is_translator': False, u'geo_enabled': True, u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/5iRhy7wTgu', u'indices': [0, 22], u'expanded_url': u'http://blog.twitter.com/', u'display_url': u'blog.twitter.com'}]}, u'description': {u'urls': [{u'url': u'https://t.co/qq1HEzvnrA', u'indices': [84, 107], u'expanded_url': u'http://support.twitter.com', u'display_url': u'support.twitter.com'}]}}, u'followers_count': 56827498, u'protected': False, u'location': u'San Francisco, CA', u'default_profile_image': False, u'id_str': u'783214', u'lang': u'en', u'utc_offset': -25200, u'statuses_count': 3161, u'description': u'Your official source for news, updates and tips from Twitter, Inc. Need help? Visit https://t.co/qq1HEzvnrA.', u'friends_count': 145, u'profile_link_color': u'226699', u'profile_image_url': u'http://pbs.twimg.com/profile_images/767879603977191425/29zfZY6I_normal.jpg', u'notifications': False, u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/657090062/l1uqey5sy82r9ijhke1i.png', u'profile_background_color': u'ACDED6', u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/783214/1471929200', u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/657090062/l1uqey5sy82r9ijhke1i.png', u'name': u'Twitter', u'is_translation_enabled': False, u'profile_background_tile': True, u'favourites_count': 2332, u'screen_name': u'twitter', u'url': u'http://t.co/5iRhy7wTgu', u'created_at': u'Tue Feb 20 14:35:54 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'profile_sidebar_border_color': u'FFFFFF', u'default_profile': False, u'following': False, u'listed_count': 90445}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'possibly_sensitive_appealable': False, u'lang': u'en', u'created_at': u'Mon Sep 19 17:00:36 +0000 2016', u'in_reply_to_status_id_str': None, u'place': None}
test_tweet_extended_object = {u'full_text': u"Say more about what's happening! Rolling out now: photos, videos, GIFs, polls, and Quote Tweets no longer count toward your 140 characters. https://t.co/I9pUC0NdZC", u'truncated': False, u'is_quote_status': False, u'in_reply_to_status_id': None, u'id': 777915304261193728, u'favorite_count': 13856, u'contributors': None, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': [], u'media': [{u'expanded_url': u'https://twitter.com/twitter/status/777915304261193728/photo/1', u'sizes': {u'small': {u'h': 340, u'w': 340, u'resize': u'fit'}, u'large': {u'h': 700, u'w': 700, u'resize': u'fit'}, u'medium': {u'h': 600, u'w': 600, u'resize': u'fit'}, u'thumb': {u'h': 150, u'w': 150, u'resize': u'crop'}}, u'url': u'https://t.co/I9pUC0NdZC', u'media_url_https': u'https://pbs.twimg.com/tweet_video_thumb/Csu1TzEVMAAAEv7.jpg', u'id_str': u'777914712382058496', u'indices': [140, 163], u'media_url': u'http://pbs.twimg.com/tweet_video_thumb/Csu1TzEVMAAAEv7.jpg', u'type': u'photo', u'id': 777914712382058496, u'display_url': u'pic.twitter.com/I9pUC0NdZC'}]}, u'in_reply_to_screen_name': None, u'id_str': u'777915304261193728', u'display_text_range': [0, 139], u'retweet_count': 14767, u'in_reply_to_user_id': None, u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'id': 783214, u'verified': True, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/767879603977191425/29zfZY6I_normal.jpg', u'profile_sidebar_fill_color': u'F6F6F6', u'is_translator': False, u'geo_enabled': True, u'entities': {u'url': {u'urls': [{u'url': u'http://t.co/5iRhy7wTgu', u'indices': [0, 22], u'expanded_url': u'http://blog.twitter.com/', u'display_url': u'blog.twitter.com'}]}, u'description': {u'urls': [{u'url': u'https://t.co/qq1HEzvnrA', u'indices': [84, 107], u'expanded_url': u'http://support.twitter.com', u'display_url': u'support.twitter.com'}]}}, u'followers_count': 56827498, u'protected': False, u'location': u'San Francisco, CA', u'default_profile_image': False, u'id_str': u'783214', u'lang': u'en', u'utc_offset': -25200, u'statuses_count': 3161, u'description': u'Your official source for news, updates and tips from Twitter, Inc. Need help? Visit https://t.co/qq1HEzvnrA.', u'friends_count': 145, u'profile_link_color': u'226699', u'profile_image_url': u'http://pbs.twimg.com/profile_images/767879603977191425/29zfZY6I_normal.jpg', u'notifications': False, u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/657090062/l1uqey5sy82r9ijhke1i.png', u'profile_background_color': u'ACDED6', u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/783214/1471929200', u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/657090062/l1uqey5sy82r9ijhke1i.png', u'name': u'Twitter', u'is_translation_enabled': False, u'profile_background_tile': True, u'favourites_count': 2332, u'screen_name': u'twitter', u'url': u'http://t.co/5iRhy7wTgu', u'created_at': u'Tue Feb 20 14:35:54 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'profile_sidebar_border_color': u'FFFFFF', u'default_profile': False, u'following': False, u'listed_count': 90445}, u'geo': None, u'in_reply_to_user_id_str': None, u'possibly_sensitive': False, u'possibly_sensitive_appealable': False, u'lang': u'en', u'created_at': u'Mon Sep 19 17:00:36 +0000 2016', u'in_reply_to_status_id_str': None, u'place': None, u'extended_entities': {u'media': [{u'expanded_url': u'https://twitter.com/twitter/status/777915304261193728/photo/1', u'display_url': u'pic.twitter.com/I9pUC0NdZC', u'url': u'https://t.co/I9pUC0NdZC', u'media_url_https': u'https://pbs.twimg.com/tweet_video_thumb/Csu1TzEVMAAAEv7.jpg', u'video_info': {u'aspect_ratio': [1, 1], u'variants': [{u'url': u'https://pbs.twimg.com/tweet_video/Csu1TzEVMAAAEv7.mp4', u'bitrate': 0, u'content_type': u'video/mp4'}]}, u'id_str': u'777914712382058496', u'sizes': {u'small': {u'h': 340, u'w': 340, u'resize': u'fit'}, u'large': {u'h': 700, u'w': 700, u'resize': u'fit'}, u'medium': {u'h': 600, u'w': 600, u'resize': u'fit'}, u'thumb': {u'h': 150, u'w': 150, u'resize': u'crop'}}, u'indices': [140, 163], u'type': u'animated_gif', u'id': 777914712382058496, u'media_url': u'http://pbs.twimg.com/tweet_video_thumb/Csu1TzEVMAAAEv7.jpg'}]}}
test_tweet_extended_html = 'Say more about what\'s happening! Rolling out now: photos, videos, GIFs, polls, and Quote Tweets no longer count toward your 140 characters.<span class="twython-tweet-suffix"> <a href="https://t.co/I9pUC0NdZC" class="twython-media">pic.twitter.com/I9pUC0NdZC</a></span>'

test_tweet_identical_urls = {u'entities': {u'hashtags': [], u'user_mentions': [], u'symbols': [], u'urls': [{u'display_url': u'buff.ly/2sEhrgO', u'expanded_url': u'http://buff.ly/2sEhrgO', u'indices': [42, 65], u'url': u'https://t.co/W0uArTMk9N'}, {u'display_url': u'buff.ly/2sEhrgO', u'expanded_url': u'http://buff.ly/2sEhrgO', u'indices': [101, 124], u'url': u'https://t.co/W0uArTMk9N'}]}, u'full_text': u'Use Cases, Trials and Making 5G a Reality https://t.co/W0uArTMk9N #5G #innovation via @5GWorldSeries https://t.co/W0uArTMk9N'}

