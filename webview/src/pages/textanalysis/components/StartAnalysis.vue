<template>
  <div class="outer">
    <div class="middle">
      <div class="logo">
        <svg class="svg" width="40px" height="40px" viewBox="0 0 64 64" version="1.1">
          <title>Icon</title>
          <defs>
            <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="linearGradient-1">
              <stop stop-color="#FFFFFF" offset="0%"></stop>
              <stop stop-color="#F2F2F2" offset="100%"></stop>
            </linearGradient>
            <circle id="path-2" cx="31.9988602" cy="31.9988602" r="2.92886048"></circle>
            <filter x="-85.4%" y="-68.3%" width="270.7%" height="270.7%" filterUnits="objectBoundingBox" id="filter-3">
              <feOffset dx="0" dy="1" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
              <feGaussianBlur stdDeviation="1.5" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
              <feColorMatrix values="0 0 0 0 0   0 0 0 0 0   0 0 0 0 0  0 0 0 0.159703351 0" type="matrix"
                in="shadowBlurOuter1"></feColorMatrix>
            </filter>
          </defs>
          <g id="slogo" class="rotation" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
            <g>
              <g id="Icon">
                <circle id="Oval-1" fill="url(#linearGradient-1)" cx="32" cy="32" r="32"></circle>
                <path
                  d="M36.7078009,31.8054514 L36.7078009,51.7110548 C36.7078009,54.2844537 34.6258634,56.3695395 32.0579205,56.3695395 C29.4899777,56.3695395 27.4099998,54.0704461 27.4099998,51.7941246 L27.4099998,31.8061972 C27.4099998,29.528395 29.4909575,27.218453 32.0589004,27.230043 C34.6268432,27.241633 36.7078009,29.528395 36.7078009,31.8054514 Z"
                  id="blue" fill="#2359F1" fill-rule="nonzero"></path>
                <path
                  d="M45.2586091,17.1026914 C45.2586091,17.1026914 45.5657231,34.0524383 45.2345291,37.01141 C44.9033351,39.9703817 43.1767091,41.6667796 40.6088126,41.6667796 C38.040916,41.6667796 35.9609757,39.3676862 35.9609757,37.0913646 L35.9609757,17.1034372 C35.9609757,14.825635 38.0418959,12.515693 40.6097924,12.527283 C43.177689,12.538873 45.2586091,14.825635 45.2586091,17.1026914 Z"
                  id="green" fill="#57CF27" fill-rule="nonzero"
                  transform="translate(40.674608, 27.097010) rotate(60.000000) translate(-40.674608, -27.097010) ">
                </path>
                <path
                  d="M28.0410158,17.0465598 L28.0410158,36.9521632 C28.0410158,39.525562 25.9591158,41.6106479 23.3912193,41.6106479 C20.8233227,41.6106479 18.7433824,39.3115545 18.7433824,37.035233 L18.7433824,17.0473055 C18.7433824,14.7695034 20.8243026,12.4595614 23.3921991,12.4711513 C25.9600956,12.4827413 28.0410158,14.7695034 28.0410158,17.0465598 Z"
                  id="red" fill="#FF561B" fill-rule="nonzero"
                  transform="translate(23.392199, 27.040878) rotate(-60.000000) translate(-23.392199, -27.040878) ">
                </path>
                <g id="inner-round">
                  <use fill="black" fill-opacity="1" filter="url(#filter-3)" xlink:href="#path-2"></use>
                  <use fill="#F7F7F7" fill-rule="evenodd" xlink:href="#path-2"></use>
                </g>
              </g>
            </g>
          </g>
        </svg>
        <span class="name">情感分析API</span>
      </div>
      <p>输入一段想分析的文字：
        <a @click="changetext">随机一段文字示例？</a>
        <i class="el-icon-circle-close-outline" @click="cleartext"></i>
      </p>

      <el-input class="text" type="textarea" :rows="10" placeholder="请输入内容" v-model="textarea">
      </el-input>
    </div>
    <div class="show">
      <el-row :gutter="20">
        <el-col :span="8">
          <div class="grid-content">
            <ve-funnel :data="chartDataf" :legend-visible="false" height="315px" class="charts-f"></ve-funnel>
          </div>
        </el-col>
        <el-col :span="8">
          <div v-if="this.sentiments" class="grid-content bg-content">
            <el-progress class="progress" v-if="this.sentiments>50" type="circle" :percentage="this.sentiments"
              color="#13ce66" status="text">
              {{this.sentiments + '%'}}积极
            </el-progress>
            <el-progress class="progress" v-else type="circle" :percentage="this.sentiments" color="#ff4949"
              status="text">
              {{this.sentiments + '%'}}消极
            </el-progress>
          </div>
          <div v-else class="grid-content">
            <el-progress class="progress" type="circle" :percentage="0" status="text">
              0%消极
            </el-progress>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content">
            <ve-pie :data="chartData" :settings="chartSettings" :legend-visible="false" height="315px" class="charts">
            </ve-pie>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'StartAnalysis',
  data () {
    this.chartSettings = {
      dimension: '关键词',
      metrics: '数量'
    }
    return {
      textarea: '',
      sentiments: '',
      chartData: {
        columns: ['关键词', '数量'],
        rows: [{
          '关键词': '1',
          '数量': 1538
        },
        {
          '关键词': '2',
          '数量': 3512
        },
        {
          '关键词': '3',
          '数量': 2432
        }]
      },
      chartDataf: {
        columns: ['状态', '数值'],
        rows: [{
          '状态': '',
          '数值': 0.9
        },
        {
          '状态': '',
          '数值': 0.6
        },
        {
          '状态': '',
          '数值': 0.3
        },
        {
          '状态': '',
          '数值': 0.1
        },
        {
          '状态': '',
          '数值': 0.1
        }]
      },
      text: [
        '【辣眼睛！大庭广众之下合肥地铁站内一对情侣抱起做出如此不雅行为！】网友反映：8月22日晚18点52分，合肥地铁一号线一对情侣竟在大庭广众之下做出如此不雅行为！',
        '网易云,谁给你的权利跟资格占用我的锁屏？你安装的时候好像没经过我同意吧？',
        '恩爱还是要秀一下的，怎么说都属于正能量！',
        '我在感情里好怕#被人有所保留的对待#啊！要不你就踏踏实实诚心诚意的对我，要不就完全放弃我，不要一会给一点甜，我也不知道这是你的全部，还是我就值得这么多。我诚惶诚恐的留下，又舍不得走。 ',
        '热爱电影敢于不同,不管是60后还是00后，能够因为电影坐在一起无代沟聊天，真好。',
        '又到了这个时间，精神抖擞，思维奔逸。开始思考人类的大事，想向宇宙发射讯号，人类到底有没有灵魂，我们存在的意义是什么，人生的苦究竟什么时候是个头。费解，怎么这么多有意思的事情争先恐后等着我解决，晚上了不起。',
        '【研究生美女买奔驰漏油大闹4S】Part 1 西安某奔驰4S店，小姑娘买车没出门车就漏油，15天忽悠协商最后给出三包换发动机的答复。逼得小姑娘只能去求曝光，声泪俱下..不管你开没有开车贷必须继续还..退款不可能..各种各样投诉无门..车商和媒体关系非一般充值到位只手遮天',
        '这季后赛太精彩了 JDG每一场准备都这么好的吗 ​​​'
      ]

    }
  },
  methods: {
    cleartext () {
      this.textarea = ''
    },
    changetext () {
      this.textarea = this.text[parseInt(Math.random() * 7)]
    }
  },
  mounted () {
    this.changetext()
  },
  watch: {
    'textarea': function (newval) {
      if (newval !== '') {
        axios.get('http://localhost:8000/snownlpapi?&snownlp=' + newval)
          .then((response) => {
            console.log(response.data)
            this.sentiments = parseInt(parseFloat(response.data.sentiments) * 100)
            this.chartData.rows = [{
              '关键词': response.data.keywords[0],
              '数量': Math.random() * 300
            },
            {
              '关键词': response.data.keywords[1],
              '数量': Math.random() * 200
            },
            {
              '关键词': response.data.keywords[2],
              '数量': Math.random() * 100
            }]
            this.chartDataf.rows = [{
              '状态': response.data.tf[0][0],
              '数值': response.data.tf[0][1]
            },
            {
              '状态': response.data.tf[1][0],
              '数值': response.data.tf[1][1]
            },
            {
              '状态': response.data.tf[2][0],
              '数值': response.data.tf[2][1]
            },
            {
              '状态': response.data.tf[3][0],
              '数值': response.data.tf[3][1]
            },
            {
              '状态': response.data.tf[4][0],
              '数值': response.data.tf[4][1]
            }]
          })
      }
    }
  }
}

</script>

<style lang="scss" scoped>
  .logo {
    text-align: center;

    .svg {
      vertical-align: middle;
    }

    @-webkit-keyframes rotation {
      from {
        -webkit-transform: rotate(0deg);
      }

      to {
        -webkit-transform: rotate(360deg);
      }
    }

    .rotation {
      -webkit-transform: rotate(360deg);
      animation: rotation 3s linear infinite;
      -moz-animation: rotation 3s linear infinite;
      -webkit-animation: rotation 3s linear infinite;
      -o-animation: rotation 3s linear infinite;
      transform-origin: center center;
    }

    .name {
      vertical-align: middle;
      font-size: .48rem;
      margin-left: .24rem;
      font-weight: 200;
      color: #fff;
    }
  }

  .middle {
    position: relative;
    top: 30px;
    min-width: 800px;
    max-width: 900px;
    margin: 0 auto;

    .text {
      font-size: 16px;
      font-family: "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    }

    p {
      font-size: 16px;
      color: #fff;
      text-align: left;
      position: relative;

      i {
        float: right;
        color: #fff;
        font-size: 30px;
        cursor: pointer;
      }

      a {
        text-decoration: underline;
        font-size: 14px;
        color: #cccccc;
        cursor: pointer;
      }
    }
  }

  .el-row {
    margin-bottom: 20px;

    &:last-child {
      margin-bottom: 0;
    }
  }

  .el-col {
    border-radius: 4px;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    position: relative;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

  .show {
    max-width: 1100px;
    margin: 80px auto 20px;
    text-align: center;
    position: relative;

    .progress {
      transform: scale(1.6);
      margin-top: 45px;
    }

    .charts-f {
      margin-top: -67px;
    }

    .charts {
      margin-top: -117px;
    }
  }

</style>
