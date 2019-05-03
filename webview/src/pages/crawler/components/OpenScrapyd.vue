<template>
  <div class="outer">
    <el-row :gutter="20">
      <el-col :span="10">
        <div class="grid-content grid-left">
          <div class="logo">
            <svg class="svg" width="72px" height="72px" viewBox="0 0 64 64" version="1.1">
              <title>Icon</title>
              <defs>
                <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="linearGradient-1">
                  <stop stop-color="#FFFFFF" offset="0%"></stop>
                  <stop stop-color="#F2F2F2" offset="100%"></stop>
                </linearGradient>
                <circle id="path-2" cx="31.9988602" cy="31.9988602" r="2.92886048"></circle>
                <filter x="-85.4%" y="-68.3%" width="270.7%" height="270.7%" filterUnits="objectBoundingBox"
                  id="filter-3">
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
            <span class="name">Scrapyd持续爬虫API</span>
          </div>
          <p class="logo-txt">Scrapyd服务器状态</p>
          <p class="logo-txt">{{currentDate}}</p>
          <p class="logo-txt">服务名称：{{this.scrapyd.name}}</p>
          <p class="logo-txt">状态：{{this.scrapyd.status}}</p>
          <p class="logo-txt">运行中数量：{{this.scrapyd.running}}</p>
          <p class="logo-txt">等待运行数量：{{this.scrapyd.pending}}</p>
          <p class="logo-txt">已完成数量：{{this.scrapyd.finished}}</p>
          <p class="logo-txt">最新工作id：{{this.scrapyd.jobId}}</p>
          <p class="logo-txt">scrapy已部署在scrapyd上</p>
          <p class="logo-txt">重新部署命令scrapyd-deploy sina -p bot</p>
          <p class="logo-txt">在右侧输入信息启动爬虫吧</p>
        </div>
      </el-col>
      <el-col :span="14">
        <div class="grid-content">
          <el-form ref="form" :model="form" :rules="rules" class="ruleForm">
            <el-form-item label="爬虫微博ID(多账号用逗号隔开)" prop="wbid">
              <el-input v-model="form.wbid" name="wbid"></el-input>
            </el-form-item>
            <el-form-item label="微博Cookie" prop="cookie">
              <el-input type="textarea" :rows="8" v-model="form.cookie" name="cookie"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit('form')">启动持续爬虫</el-button>
              <el-button>取消</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'

export default {
  name: 'OpenScrapyd',
  data () {
    return {
      currentDate: new Date(),
      scrapyd: {
        status: '❌',
        name: '😭',
        finished: '😭',
        pending: '😭',
        running: '😭',
        jobId: '此信息需要右侧启动爬虫才可显示'
      },
      form: {
        wbid: '',
        cookie: ''
      },
      rules: {
        wbid: [{
          required: true,
          message: '请输入爬虫微博用户id',
          trigger: 'blur'
        },
        {
          min: 10,
          message: '长度不正确',
          trigger: 'blur'
        }],
        cookie: [{
          required: true,
          message: '请填写Cookie',
          trigger: 'blur'
        }]
      }
    }
  },
  methods: {
    onSubmit (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let reg = new RegExp('^[0-9+,+，]*$')
          if (!reg.test(this.form.wbid)) {
            this.open('微博Id请输入纯数字')
          } else {
            this.form.wbid = this.form.wbid.replace('，', ',')
            axios.post('http://localhost:8000/scrapydapi/',
              Qs.stringify({
                weiboIds: this.form.wbid,
                cookies: this.form.cookie
              })
            ).then((response) => {
              console.log(response.data)
              if (response.data.status === 'ok') {
                this.scrapyd.jobId = response.data.jobid
                this.getScrapyd()
                this.$notify({
                  title: '启动持续爬虫成功',
                  dangerouslyUseHTMLString: true,
                  message: '左侧查看服务器状态信息 or <br><a target="_blank" href="http://localhost:6800/jobs">点击进入爬虫服务器</a>',
                  type: 'success',
                  duration: 0
                })
              }
            })
          }
        } else {
          this.open('请输入正确的信息!!')
          return false
        }
      })
    },
    getScrapyd () {
      axios.get('http://localhost:8000/scrapydapi/')
        .then((response) => {
          console.log(response.data)
          // if (response.data.status === 'ok') {
          //   this.scrapyd.status = '👌'
          // } else {
          //   this.scrapyd.status = response.data.status
          // }
          this.scrapyd.status = response.data.status
          this.scrapyd.name = response.data.node_name
          this.scrapyd.finished = response.data.finished
          this.scrapyd.pending = response.data.pending
          this.scrapyd.running = response.data.running
        })
        .catch((error) => {
          this.$message.error('请检查Scrpayd服务器是否正常运行！！', error)
        })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    open (message) {
      this.$message.error(message)
    }
  },
  mounted () {
    let _this = this
    this.timer = setInterval(() => {
      _this.currentDate = new Date()
    }, 1000)
    this.getScrapyd()
  },
  beforeDestroy () {
    if (this.timer) {
      clearInterval(this.timer)
    }
  }
}

</script>

<style lang="scss" scoped>
  .outer {
    min-width: 1100px;
    max-width: 1200px;
    margin: 50px auto 0;
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

  .bg-purple-dark {
    background: #99a9bf;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content {
    border-radius: 4px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

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

  .grid-left {
    padding: .46rem 0;
  }

  .logo-txt {
    position: relative;
    top: 0;
    font-size: .28rem;
    text-align: center;
    font-weight: 200;
    line-height: .1rem;
    color: #fff;
  }

  .el-form {
    vertical-align: middle;
  }

  .ruleForm {
    padding: 30px 30px 0;
    /deep/ .el-form-item__label {
      color: #fff;
    }
  }

</style>
