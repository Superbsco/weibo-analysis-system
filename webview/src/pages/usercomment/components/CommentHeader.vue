<template>
  <div>
    <!-- {{this.usercomment.mingan}} -->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span class="title">微博传播效果分析 | 阅读</span>
        <router-link to="/comment">
          <p class="title-analysis">还想继续分析？</p>
        </router-link>
        <!-- <el-button class="finstatus" type="text">微博文本情感，评论偏消极</el-button> -->
      </div>
      <div class="mwbcon">
        <div class="m_l v_yellow">
          <img id="weiboContentUserHead" style="cursor: pointer;" :src="this.userInfo[0].fields.wb_user_profile_image_url">
        </div>
        <div class="m_r">
          <p id="weiboContentUserNickname">
            <a class="mscrame" href="javascript:;" @click="website(userId)" target="_blank">{{this.userInfo[0].fields.wb_userName}}</a>
          </p>
          <div class="mwbcontext" id="weiboContentPic">
            <p v-html="this.userText" ref='cvs'></p>
            <img v-for="(img, index) in this.userImg" :key="index" :src="setImg(img)" :class="imglen" preview="1">
          </div>
          <div class="mfont-buttom" id="weiboContentButtomTime" style="display: block;">
            <div class="mfont-buttom_l" id="weiboContentTime" style="bottom: 20px;padding-top: 0px;">
              <span style="cursor: pointer;" @click="website(wburl)">{{this.userInfo[0].fields.wb_created_at}}</span>
              <span>分析时间：{{dateFormat(create_time)}}</span>
              <span v-if="this.userInfo[0].fields.wb_source">来自{{this.userInfo[0].fields.wb_source}}</span>
            </div>
            <div class="mfont-buttom_r" style="bottom: 20px; right: 20px; z-index: 4;padding-top: 0px;">
              <a class="weibo-multi-panel weibo-list-a" id="weiboContentForwardNumber">转发({{this.userInfo[0].fields.wb_reposts}})</a> |
              <a class="weibo-multi-panel weibo-list-a" id="weiboContentCommentNumber">评论({{this.userInfo[0].fields.wb_comments}})</a> |
              <a class="weibo-multi-panel weibo-list-a" id="weiboContentPraiseNumber">赞({{this.userInfo[0].fields.wb_like}})</a>
            </div>
          </div>
        </div>
        <div class="clear explain" id="weiboContentNote" style="display: block; bottom: 10px;"><strong style="color:#B94A48">数据说明：</strong>系统分析的数据来自微博的最高层级的转发及评论数据。</div>
      </div>
      <div class="row-fluid">
        <div class="mwbcon" id="all_dec">
          <div class="well fz14" style="padding: 15px 2px;font-size: 13px;margin-bottom: 0;background-color:#f7f9fa !important">
            截至分析时间<strong id="analysis_time">{{dateFormat(create_time)}}</strong>，@<strong id="bloger">{{this.userInfo[0].fields.wb_userName}}</strong> 的微博共收获转发数<strong id="transNum">{{this.userInfo[0].fields.wb_reposts}}</strong>次（其中有效转发<strong id="repostsUserCount">{{this.userInfo[0].fields.wb_reposts}}</strong>次）、
            评论数<strong id="comment">{{this.userInfo[0].fields.wb_comments}}</strong>条（其中有效评论<strong id="repostsUserCount">{{this.commentInfo.length}}</strong>条），点赞数<strong id="likeNum">{{this.userInfo[0].fields.wb_like}}</strong>个；@<strong id="keyUserName">{{this.commentInfo[0].fields.c_user_name}}</strong> 评论微博并成为关键传播用户。
          </div>
        </div>
      </div>
      <div class="row-fluid">
        <div class="mwbcon">
          <p class="c-title">评论趋势图</p>
        </div>
        <ve-line :data="this.commentchart" :settings="chartSettings"></ve-line>
        <div class="well fz14" style="padding: 15px 2px;font-size: 13px;margin-bottom: 0;background-color:#f7f9fa !important">
          该微博始发于<strong id="analysis_time">{{this.usercomment.commentqushi[10].date.replace(/"/g, '')}}</strong>，于<strong id="bloger">{{maxComment()}}</strong> 评论数达到最高峰<strong id="transNum">{{this.usercomment.commentqushi[10].count}}</strong>。
        </div>
      </div>
      <div class="row-fluid">
        <div class="mwbcon">
          <p class="c-title">用户引爆点</p>
        </div>
        <el-table
          :data="this.tableData"
          style="width: 100%"
          :row-class-name="tableRowClassName">
          <el-table-column
            prop="date"
            label="时间"
            width="150">
          </el-table-column>
          <el-table-column
            prop="name"
            label="昵称"
            width="100">
          </el-table-column>
          <el-table-column
            prop="content"
            label="内容">
          </el-table-column>
          <el-table-column
            prop="like"
            label="点赞数"
            width="80">
          </el-table-column>
        </el-table>
      </div>
      <div class="row-fluid">
        <div class="mwbcon">
          <p class="c-title">评论词云</p>
        </div>
        <ve-wordcloud :data="getRows()" :settings="chartSettings1"></ve-wordcloud>
        <div class="well fz14" style="padding: 15px 2px;font-size: 13px;margin-bottom: 0;background-color:#f7f9fa !important">
          该微博的评论中，词汇<strong id="analysis_time">{{this.usercomment.cipin[0].word}}</strong>频率最高，达到<strong id="bloger">{{this.usercomment.cipin[0].count}}</strong> 次。
          其次是<strong id="analysis_time">{{this.usercomment.cipin[1].word}}、{{this.usercomment.cipin[2].word}}、{{this.usercomment.cipin[3].word}}</strong>分别达到
          <strong id="bloger">{{this.usercomment.cipin[1].count}}、{{this.usercomment.cipin[2].count}}、{{this.usercomment.cipin[3].count}}</strong> 次。
        </div>
      </div>
      <div class="row-fluid">
        <div class="mwbcon">
          <p class="c-title">评论敏感率（当前敏感率只检测暴恐、反动、民生、色情等词汇）</p>
        </div>
        <ve-bar :data="minganData()" height="3.4rem"></ve-bar>
        <div class="well fz14" style="padding: 15px 2px;font-size: 13px;margin-bottom: 0;background-color:#f7f9fa !important">
          该微博的评论中，敏感占比<strong>{{this.usercomment.mingan.toFixed(2)}}%</strong>,
          在<strong>
            <span v-if="this.usercomment.mingan.toFixed(2) < 0.25">极低</span>
            <span v-else-if="this.usercomment.mingan.toFixed(2) >= 0.25 && this.usercomment.mingan.toFixed(2) < 0.5">低</span>
            <span v-else-if="this.usercomment.mingan.toFixed(2) >= 0.5  && this.usercomment.mingan.toFixed(2) < 0.75">高</span>
            <span v-else>极高</span>
          </strong>敏感范围内
        </div>
      </div>
      <div class="row-fluid">
        <div class="mwbcon">
          <p class="c-title">评论内容情感分析</p>
          <ve-histogram :data="chartData" :settings="chartSettings2"></ve-histogram>
        </div>
        <div class="well fz14" style="padding: 15px 2px;font-size: 13px;margin-bottom: 0;background-color:#f7f9fa !important">
          根据该微博评论的情感分析情况：
          消极评论最小值<strong>{{ this.emtionanaly.smalldate }} </strong>
          ，次数是<strong>{{ this.emtionanaly.smallcount }} </strong>；
          积极评论最大值<strong>{{ this.emtionanaly.bigdate }} </strong>
          ，次数是<strong>{{ this.emtionanaly.bigcount }} </strong>；
          最大的评论次数是<strong>{{ this.emtionanaly.maxcount }} </strong>次
          ，情感值是<strong>{{ this.emtionanaly.maxdate }} </strong>。
          全部评论中：消极评论内容占比<strong>{{ (this.emtionanaly.count0 / this.emtionanaly.len)*100 }}%</strong>，
          积极评论内容占比<strong>{{ (this.emtionanaly.count1 / this.emtionanaly.len)*100 }}%</strong>。
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'
import {
  mapState
} from 'vuex'

export default {
  name: 'CommentHeader',
  data () {
    this.chartSettings = {
      stack: { '用户': ['评论用户'] },
      area: true
    }
    this.chartSettings1 = {
      sizeMin: 30,
      sizeMax: 60
    }
    this.chartSettings2 = {
      metrics: ['次数'],
      dimension: ['情感值']
      // yAxisType: ['percent']
    }
    return {
      create_time: Date(),
      chartData: {
        columns: ['情感值'],
        rows: [
          { '情感值': 1, '次数': 1 }
        ]
      },
      emtionanaly: {
        count0: 0,
        count1: 0,
        len: 1,
        maxdate: 0,
        maxcount: 0,
        smalldate: 0,
        smallcount: 0,
        bigdate: 0,
        bigcount: 0
      }
    }
  },
  mounted () {
    this.$notify.info({
      title: '消息',
      message: '请稍后，正在计算最终情感结果',
      position: 'bottom-right'
    })
    axios.get('http://localhost:8000/getcomment?&commentId=' + this.tempid)
      .then((response) => {
        let rows = []
        this.emtionanaly.len = response.data.length
        this.emtionanaly.smalldate = response.data[0][0]
        this.emtionanaly.smallcount = response.data[0][1]
        this.emtionanaly.bigdate = response.data[response.data.length - 1][0]
        this.emtionanaly.bigcount = response.data[response.data.length - 1][1]
        for (let i = 0; i < response.data.length; i++) {
          if (response.data[i][1] > this.emtionanaly.maxcount) {
            this.emtionanaly.maxcount = response.data[i][1]
            this.emtionanaly.maxdate = response.data[i][0]
          }
          rows.push({
            '情感值': response.data[i][0],
            '次数': response.data[i][1]
          })
          if (response.data[i][0] < 0.5) {
            this.emtionanaly.count0++
          } else {
            this.emtionanaly.count1++
          }
        }
        this.chartData.rows = rows
        this.mopen()
      })
  },
  computed: {
    ...mapState({
      usercomment: state => state.usercomment,
      tempid: state => state.tempid
    }),
    userInfo: function () {
      return eval('(' + this.usercomment.data + ')')
    },
    userId: function () {
      return 'https://weibo.com/' + this.userInfo[0].fields.wb_userId
    },
    userText: function () {
      return this.userInfo[0].fields.wb_text.replace('data-hide=""', 'target="_blank"').replace(/1rem/g, '.3rem')
    },
    userImg: function () {
      return eval('(' + this.userInfo[0].fields.wb_pic_ids + ')')
    },
    imglen: function () {
      if (this.userImg.length === 1) {
        return 'wb-img1'
      } else if (this.userImg.length === 2) {
        return 'wb-img2'
      } else {
        return 'wb-img3'
      }
    },
    wburl: function () {
      return 'https://m.weibo.cn/' + this.userInfo[0].fields.wb_userId + '/' + this.userInfo[0].pk
    },
    commentInfo: function () {
      return eval('(' + this.usercomment.info + ')')
    },
    commentchart: function () {
      let mrows = []
      for (let i = 0; i < 10; i++) {
        mrows.push({
          '日期': this.usercomment.commentqushi[i].date.replace(/"/g, ''),
          '评论用户': this.usercomment.commentqushi[i].count
        })
      }
      let mchartData = {
        columns: ['日期', '评论用户'],
        rows: mrows
      }
      return mchartData
    },
    tableData: function () {
      let date = []
      for (let i = 0; i < 10; i++) {
        date.push({
          date: this.commentInfo[i].fields.c_created_at,
          name: this.commentInfo[i].fields.c_user_name,
          content: this.commentInfo[i].fields.c_text,
          like: this.commentInfo[i].fields.c_like_num
        })
      }
      return date
    }
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    website: function (url) {
      window.open(url)
    },
    maxComment: function () {
      for (let i = 0; i < this.usercomment.commentqushi.length; i++) {
        if (this.usercomment.commentqushi[10].count === this.usercomment.commentqushi[i].count) {
          return this.usercomment.commentqushi[i].date.replace(/"/g, '')
        }
      }
    },
    dateFormat: function () {
      let date = new Date()
      let year = date.getFullYear()
      let month = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1
      let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      let hours = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
      let minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
      let seconds = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds()
      return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds
    },
    setImg: function (src) {
      return '/static/' + src + '.jpg'
    },
    getRows () {
      let res = []
      for (let i = 0; i < this.usercomment.cipin.length; i++) {
        res.push({
          'word': this.usercomment.cipin[i].word,
          'count': this.usercomment.cipin[i].count
        })
      }
      let chartData = {
        columns: ['word', 'count'],
        rows: res
      }
      return chartData
    },
    minganData () {
      let chartData = {
        columns: ['敏感程度', '敏感', '非敏感'],
        rows: [
          { '敏感程度': '敏感程度', '敏感': this.usercomment.mingan.toFixed(2), '非敏感': 1 - this.usercomment.mingan.toFixed(2) }
        ]
      }
      return chartData
    },
    mopen () {
      if (this.$refs.cvs.innerText) {
        console.log(this.$refs.cvs.innerText)
        axios.get('http://localhost:8000/snownlpapi?&snownlp=' + this.$refs.cvs.innerText.replace(/#/g, ''))
          .then((response) => {
            console.log(response.data)
            let success = '积极😁'
            if (response.data.sentiments > 0.5) {
              success = '积极😁'
            } else {
              success = '消极😭'
            }
            let pl = '消极偏多😭'
            if (this.emtionanaly.count0 > this.emtionanaly.count1) {
              pl = '消极偏多😭'
            } else {
              pl = '积极偏多😁'
            }
            this.$notify({
              title: '成功',
              dangerouslyUseHTMLString: true,
              message: '微博情感值：' + response.data.sentiments + '<br>情感评定：' + success + '<br>关键词是：' + response.data.keywords + '<br>评论倾向：' + pl,
              type: 'success',
              position: 'bottom-right',
              duration: 0
            })
          })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  .clear {
    clear: both;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both;
  }

  .box-card {
    width: 70%;
    position: relative;
    margin: 0 auto;
  }

  .title {
    font-size: 16px;
    padding: 15px 10px 15px 50px;
    margin: 0 0 10px;
    color: #FFF;
    text-align: center;
    background-color: #F8661E;
    background-image: url('../../../assets/icon-wyq.png');
    background-repeat: no-repeat;
    background-position: 10px center;
    padding-left: 50px;
    border-radius: 3px;
  }

  .title-analysis {
    font-size: 17px;
    margin-left: 30px;
    display: inline-block;
    color: #1d77b4;
    margin-top: 10px;
    margin-bottom: 10px;
    cursor: pointer;
  }

  .title-analysis:hover {
    text-decoration: underline;
  }

  .mwbcon .m_l > img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }

  img {
    margin: 0px;
    padding: 0px;
    list-style-type: none;
    border-style: none;
    vertical-align: middle;
    outline: none;
    border: 1px solid rgba(216, 134, 10, 0.2);
  }

  div {
    margin: 0 auto;
  }

  div.v_blue, div.v_yellow {
    position: relative;
  }

  div.v_yellow:after {
    background-image: url('../../../assets/v_yellow.png');
  }

  div.v_blue:after, div.v_yellow:after {
    content: "";
    text-align: center;
    width: 20px;
    height: 20px;
    position: absolute;
    bottom: -4px;
    left: 40px;
    background-position: center;
    background-repeat: no-repeat;
  }

  .mwbcon .m_r {
    margin-left: 80px;
    font-size: 14px;
  }

  p {
    margin: 0px;
    padding: 0px;
    border: currentColor;
    list-style-type: none;
  }

  .mwbcon {
    padding: 10px;
    overflow: hidden;
  }

  .mwbcon .m_l {
    width: 50px;
    float: left;
  }
  .mwbcontext {
    padding-top: 10px;
    line-height: 25px;
    font-size: 16px;
  }

  .mfont-buttom_l > span {
    margin-right: 30px;
  }

  .mfont-buttom {
    color: #666;
    font-size: 12px;
    line-height: 30px;
    width: 100%;
    display: inline-block;
  }

  .mscrame {
    font-size: 18px;
  }

  .mfont-buttom_r {
    float: right;
  }

  .mfont-buttom_l {
    float: left;
  }

  .explain {
    font-size: 12px;
    color: #999;
    margin-top: 10px;
    display: inline-block;
    width: 100%;
  }

  .wb-img3 {
    margin: .2rem 0;
    width: 100px;
    height: 100px;
    cursor: pointer;
  }

  .wb-img2 {
    margin: .2rem 0;
    width: 150px;
    height: 150px;
    cursor: pointer;
  }

  .wb-img1 {
    margin: .2rem 0;
    max-width: 300px;
    cursor: pointer;
  }

  .row-fluid {
    border-bottom: 1px solid #E4E7ED;
  }

  .c-title {
    font-size: 18px;
    color: #1d77b4;
    margin: 15px 0;
  }

  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

</style>
