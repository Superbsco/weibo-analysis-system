<template>
  <el-timeline class="mytimestamp">
    <el-timeline-item timestamp="快速爬虫用户" color="#E6A23C" placement="top">
      <el-card>
        <ul class="img-style">
          <li v-for="(info, index) in infos" :key="index">
            <div class="photo-warp">
              <img :src="info.Image" class="wb-img" @click="goInWb(info._id)" :title="info.NickName">
            </div>
          </li>
        </ul>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="持续爬虫用户" color="#67C23A" placement="top">
      <el-card>
        <ul v-for="(info1, index) in infos1" :key="index" class="ulinfos1" @click="goInGroup(info1.info)">
          组{{index}}
          <li v-for="(info2, i) in infos1[index].info" :key="i">
            <img :src="info2.Image" :title="info2.nick_name">
          </li>
        </ul>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="单条微博" color="#F56C6C" placement="top">
      <el-card>
        <div v-for="(info, index) in infos2" :key="index" class="outer" @click="goInComment(info.wb_id)">
          <div class="m_l">
            <img :src="info.wb_user_profile_image_url">
          </div>
          <div class="m_r">
            <p>
              <a class="mscrame" @click="website(info.wb_userId)" href="javascript:;" target="_blank">{{info.wb_userName}}</a>
            </p>
            <div class="mwbcontext">
              <p v-html="info.wb_text" ref='cvs'></p>
            </div>
          </div>
        </div>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'

export default {
  name: 'MyScrapyd',
  data () {
    return {
      loading: '',
      infos: '',
      infos1: '',
      infos2: ''
    }
  },
  methods: {
    getQuick () {
      axios.get('http://localhost:8000/getquick/').then((response) => {
        let res = JSON.parse(response.data)
        for (let i = 0; i < res.length; i++) {
          res[i].Image = eval('(' + res[i].Image + ')')[0]
        }
        this.infos = res
      })
    },
    getLasted () {
      axios.get('http://localhost:8000/getlasted/').then((response) => {
        let res = JSON.parse(response.data.user)
        let group = JSON.parse(response.data.target)
        let count = JSON.parse(response.data.count)
        let newres = []
        for (let i = 0; i < res.length; i++) {
          for (let j = 0; j < group.length; j++) {
            if (res[i]._id === group[j].uid) {
              res[i].group = group[j].group
            }
          }
        }
        for (let k = 0; k < count.length; k++) {
          newres.push({
            'group': count[k][0],
            'info': []
          })
          for (let l = 0; l < res.length; l++) {
            if (newres[k].group === res[l].group) {
              newres[k].info.push(res[l])
            }
          }
        }
        this.infos1 = newres
      })
    },
    getWeibo () {
      axios.get('http://localhost:8000/getweibo/').then((response) => {
        let res = JSON.parse(response.data)
        for (let i = 0; i < res.length; i++) {
          res[i].wb_text = res[i].wb_text.replace('data-hide=""', 'target="_blank"').replace(/1rem/g, '.3rem')
        }
        this.infos2 = res
      })
    },
    website: function (userId) {
      window.open('https://weibo.com/' + userId)
    },
    goInComment: function (wbId) {
      this.openFullScreen2()
      axios.post('http://localhost:8000/getcomment/',
        Qs.stringify({
          commentId: wbId
        })
      ).then((response) => {
        this.$store.state.tempid = wbId
        this.$store.state.usercomment = response.data
        this.loading.close()
        this.$router.push({
          path: '/usercomment'
        })
      })
    },
    goInGroup: function (ids) {
      let group = ''
      for (let i = 0; i < ids.length; i++) {
        if (i === ids.length - 1) {
          group += ids[i]._id
        } else {
          group += ids[i]._id + ','
        }
      }
      this.openFullScreen2()
      axios.post('http://localhost:8000/getgroup/',
        Qs.stringify({
          weiboIds: group
        })
      ).then((response) => {
        console.log(response.data)
        this.$store.state.tempids = group
        this.$store.state.group = response.data
        this.loading.close()
        this.$router.push({
          path: '/usergroup'
        })
      })
      console.log(group)
    },
    goInWb: function (id) {
      this.openFullScreen2()
      axios.post('http://localhost:8000/spiderapi/',
        Qs.stringify({
          weiboId: id
        })
      ).then((response) => {
        this.$store.state.user = response.data.data
        this.$store.state.usertweets = response.data.tweets
        this.$store.state.total = response.data.total
        this.loading.close()
        this.$router.push({
          path: '/user'
        })
      })
    },
    openFullScreen2 () {
      this.loading = this.$loading({
        lock: true,
        text: '后台疯狂进行爬虫计算中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
    }
  },
  mounted () {
    this.getQuick()
    this.getLasted()
    this.getWeibo()
  }
}

</script>

<style lang="scss" scoped>
  .mytimestamp {
    width: 70%;
    max-width: 900px;
    margin: 0 auto;
  }

  /deep/ .el-timeline-item__timestamp {
    color: #fff;
  }

  .img-style {
    list-style: none;
    padding: 0;
    li {
      width: 10%;
      display: inline-block;
      .photo-warp {
        width: 60px;
        height: 60px;
        margin: 0 auto;
        border: 1px solid #fff;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        transition: all 0.6s;
        .wb-img {
          width: 60px;
          height: 60px;
          border-radius: 50%;
          display: block;
          cursor: pointer;
        }
      }
    }
  }

  .photo-warp:hover {
    transform: scale(1.2);
  }

  .m_l > img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 1px solid #fff;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    display: block;
    cursor: pointer;
  }

  .m_r {
    margin-left: 80px;
    font-size: 14px;
  }

  .m_l {
    width: 50px;
    float: left;
  }

  .mwbcontext {
    line-height: 25px;
    font-size: 15px;
  }

  .mscrame {
    font-size: 17px;
  }

  .outer {
    border-bottom: 1px solid #DCDFE6;
    cursor: pointer;
  }

  .outer:hover {
    background-color: #EBEEF5;
  }

  .ulinfos1 {
    list-style: none;
    padding: 0;
    border-bottom: 1px solid #DCDFE6;
    color: #909399;
    li {
      width: 10%;
      display: inline-block;
      img {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: block;
        cursor: pointer;
        border: 1px solid #fff;
        background: rgba(255, 255, 255, 0.3);
      }
    }
  }

  .ulinfos1:hover {
    background-color: #EBEEF5;
    cursor: pointer;
  }

</style>
