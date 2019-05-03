<template>
  <div>
    <common-header></common-header>
    <user-header></user-header>
    <scroll-top></scroll-top>
    <bg-color></bg-color>
    <common-footer></common-footer>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import ScrollTop from 'common/ScrollToTop'
import CommonFooter from 'common/Footer'
import BgColor from 'common/BgSet'
import UserHeader from './components/UserHeader'

export default {
  name: 'UserInfo',
  components: {
    CommonHeader,
    UserHeader,
    ScrollTop,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
