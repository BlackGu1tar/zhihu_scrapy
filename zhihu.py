#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
import time,re

#f=open('zhihu.txt','w',encoding='utf-8')
url_answers='https://www.zhihu.com/api/v4/questions/377861079/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&platform=desktop'

while True:
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-us",
               "Connection": "keep-alive",
               "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
               "Cookie": "_zap=ec94575a-8946-4b2d-b19c-8d6befe61296; d_c0=AGCX3ABqmhaPTmuia-f506fFl-rlBY3zqhM=|1681099675; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1681099675,1681290637,1681295378; captcha_session_v2=2|1:0|10:1681104788|18:captcha_session_v2|88:d3NDU09WU1M4TU9oQko0Y0QyVktNaTlxM2oxOUxvUUhjSmJKRTF4dDIydVl0cUJ0K2xqQmQvSEZNdVFHRHhhUA==|18826a5de05b4b32a00a52a122a228e69b3f63fc51daf54c5df1ba5fdb5134ed; gdxidpyhxdE=HOk4gaZVzLl%2FN3MtkqDZg3wsicclh%5CGt9OQZJD87E53bKJ2kcD5v50Nq2YZPwqPDk4Hl7NcJnNK3qTmsLNizw0Dfc%2Ffx51KiGUDU49Qz%2F5l6D27VCnGa2jmz6iRu93x%2F2DACublnQktEg4NBX%2B%2FQ%5CL34VqbSbXMcTXaDwgBj4dOj3hUA%3A1681105087222; YD00517437729195%3AWM_NI=YLQgQRMv%2BTnjw05exZfihnI0Eqb0N8Sl%2F6bd%2BRzHYCRjrWCC8qxs7ijOSxBflJoY6Pw9O608IBpAQc2PohR5%2BqYRLhBSJQVKn8Frj1JaLXvczweEqImy2Ar0GpgTbjIhOGI%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee99f867b48de1b1b572f89e8aa7c15f969b9a86d56babb79cbaf76aa6bcf895f82af0fea7c3b92a9b949f88d45a8faae5b5ed62b5f0fb86fb52a6b7a88fcc3c87afaed1cd3491b4e1d7e170e98eb6a9dc4992b6beb8c249fcafb894b663aa919d99c16eb096a1bab55cb5e781d7b3348b9ec0a2d469f290a189d13fe9af97b3cf64828d86b2d541aee88a93e93b8abf84b9f569baa9aba6f443afa7fea2f13c85b0a9b5e1628bb881a8cc37e2a3; YD00517437729195%3AWM_TID=CWI70nKjcy9AQERBUUaAe2mSYtfLZ54u; z_c0=2|1:0|10:1681106803|4:z_c0|92:Mi4xUlJrMkFBQUFBQUFBWUpmY0FHcWFGaGNBQUFCZ0FsVk53LTBnWlFCQ0JyeTBDQ1RuYi01NlUxMlMxNjdoa3RoX3B3|e5df20e4c81fb0bf7e1f7461a45ce091fd8ae438de57341be195f074b4416d86; q_c1=ca380705538747809f7716e12a560517|1681104835000|1681104835000; _xsrf=1331c6fe-c809-4871-8ff5-2822440ab093; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1682231570; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1682231629|1682227673; SESSIONID=She9q8rOdRgeMkfCQUhdl1ugJDdGqs5N4hd3HsUPadr; JOID=UlodAE2Fs6pJWpVQYoeHevlE_M581NHEdS2vKCbn48cnEvg0Kzk-4C5enVFskxTVBEOeAKEl7aMC7qQp2guSPA0=; osd=Ul8dCk6FtqpDWZVVYo2EevxE9s180dHOdi2qKCzk48InGPs0Ljk04y5bnVtvkxHVDkCeBaEv7qMH7q4q2g6SNg4=; tst=r"}

    res_answers = requests.get(url_answers, headers=headers).content.decode('utf-8')
    time.sleep(2)
    jsonfile_answers = json.loads(res_answers)
    next_page_answers = jsonfile_answers['paging']['is_end']
    url_answers=jsonfile_answers['paging']['next'] # 获取下一页的回答
    for data_answers in jsonfile_answers['data']:
        content_answers = data_answers['target']['content']
        imgs_content = re.findall(r'https:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?',content_answers)
        tmp_img_urls = set([later_url for _, later_url in imgs_content])
        img_urls = []
        for x in tmp_img_urls:
            if '_r.jpg' in x:
                img_urls.append(f"https://picx.zhimg.com{x}")
                response = requests.get(f"https://picx.zhimg.com{x}", headers=headers, timeout=10)
                time.sleep(0.5)
                tmp_filename = x.strip('/v2-')
                filename = tmp_filename.strip('?source=1940ef5c')
                with open(f'c:\\zhihu_pics\\{filename}', 'wb') as f:
                    f.write(response.content)
                    f.flush()
                    print(f"[+]https://picx.zhimg.com{x}下载成功！")
    if next_page_answers == True:
        break
print(f"[+]共下载{len(img_urls)}张图片！")
