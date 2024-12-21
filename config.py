# 请求的URL
URL = "https://leetcode.cn/graphql/"

# 请求头
HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "gr_user_id=c5b2ee93-faaa-49c4-baee-e6f0ca114786; _bl_uid=nFl2Oyp0e26nRzstn139wde8wbRq; a2873925c34ecbd2_gr_last_sent_cs1=117-hk; csrftoken=HnfqM4i4h3GONDVaogNxUtA9on2ondHxIQz5cQREGkpP5wg2DDkzV2YwkaQqPoTu; tfstk=fKHoBrXF-bPSfWC0mIyWTpRcF0RYFgwQR2BLJJUegrzbpbK7Jy0n5VVEeDezKy0El_FLJz3Dxqus2WerKj6nfDMJVJK7F0wQLFL9B9mSVJZCskrtK-P4bk9day5yZQ5rQFL9BKnKkDpwW437H650Arrz4_rymZrQu65r8zPVulq_LJyE8oo4AkBU8TrU0-zbYJzE8JlPI_ztLfk2yQxuPJrp_AquZyXLo9mI3OF77T4Vp9Uuq7fm4rXFLxcX_YJ_zCsYR8US2u0BCTwztfiLx4vlU2mshqqq7pXTzmit67My9OFgnzVIU0YkKmD3r5kziMBij8ZE8WcXSOEuejViEbtCu0uTrfySvGY-m5c01oPVx_y-6cHQ_YJl5rF_x4Ux7dW03WSPXs5wRSBQ0HHVO6Nzco4tJG5Y6R8RiGKDm1nQaoZ_WnxcO6Nzco49mnftd7rbfPC..; sl-session=OYNxWR4AU2ccdWePypy9zQ==; LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiNjgzMjMzMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDQ1OGIyZmUzOGY3YzYyZmI4NGM0ZmU1ZGJhZTU5NDMwNzAxN2NlM2JmZWMxYmEwNjJmMDlkNTljMmE1OGQxMyIsImlkIjo2ODMyMzMyLCJlbWFpbCI6IiIsInVzZXJuYW1lIjoiMTE3LWhrIiwidXNlcl9zbHVnIjoiMTE3LWhrIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY24vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy8xMTctaGsvYXZhdGFyXzE3MDIzMDc5NTIucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsImRldmljZV9pZCI6ImM4NzhlODhlNTM5ZWE1MWE2MTljM2I0YjEwZjgyYzdkIiwiaXAiOiIxMTEuMTguOTIuMTAwIiwiX3RpbWVzdGFtcCI6MTczMzAyOTYxOS40LjE3MzM0ODk2MjkuMjQuMC4wIiwibG9jYWxlIjoiemgtQ04ifQ.HnfqM4i4h3GONDVaogNxUtA9on2ondHxIQz5cQREGkpP5wg2DDkzV2YwkaQqPoTu",
    "Origin": "https://leetcode.cn",
    "Referer": "https://leetcode.cn/problems/string-to-integer-atoi/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "authorization;": "",
    "baggage": "sentry-environment=production,sentry-release=8f62ed3b,sentry-transaction=%2Fproblems%2F%5Bslug%5D%2F%5B%5B...tab%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=beeb12a8419843debf1a69ba0c5ba17e,sentry-sample_rate=0.03",
    "content-type": "application/json",
    "random-uuid": "d3aecd55-2f9d-91f8-493b-c83612e71311",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sentry-trace": "beeb12a8419843debf1a69ba0c5ba17e-9f96529e62e742f2-0",
    "x-csrftoken": "HnfqM4i4h3GONDVaogNxUtA9on2ondHxIQz5cQREGkpP5wg2DDkzV2YwkaQqPoTu"
}

# 原始查询语句：查询题目描述
QUERY_DESCRIPTION = '''
    query questionDetail($titleSlug: String!) {
  languageList {
    id
    name
    verboseName
  }
  statusList {
    id
    name: translatedName
  }
  question(titleSlug: $titleSlug) {
    title
    titleSlug
    questionId
    questionFrontendId
    questionTitle
    translatedTitle
    content
    translatedContent
    categoryTitle
    difficulty
    stats
    style
    contributors {
      username
      profileUrl
      avatarUrl
    }
    book {
      id
      bookName
      pressName
      source
      shortDescription
      fullDescription
      bookImgUrl
      pressImgUrl
      productUrl
    }
    companyTagStatsV2
    topicTags {
      name
      slug
      translatedName
    }
    similarQuestions
    mysqlSchemas
    dataSchemas
    frontendPreviews
    likes
    dislikes
    isPaidOnly
    status
    boundTopicId
    enableTestMode
    metaData
    enableRunCode
    enableSubmit
    envInfo
    isLiked
    nextChallengePairs
    libraryUrl
    hints
    codeSnippets {
      code
      lang
      langSlug
    }
    jsonExampleTestcases
    exampleTestcases
    sampleTestCase
    hasFrontendPreview
    editorType
  }
}
'''

# 原始查询语句：查询题目标题
QUERY_TITLE_SLUG = '''
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    hasMore
    total
    questions {
      acRate
      difficulty
      freqBar
      frontendQuestionId
      isFavor
      paidOnly
      solutionNum
      status
      title
      titleCn
      titleSlug
      topicTags {
        name
        nameTranslated
        id
        slug
      }
      extra {
        hasVideoSolution
        topCompanyTags {
          imgUrl
          slug
          numSubscribed
        }
      }
    }
  }
}
'''
