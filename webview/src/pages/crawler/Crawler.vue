<template>
  <div>
    <common-header></common-header>
    <open-scrapyd></open-scrapyd>
    <common-footer></common-footer>
    <bg-color></bg-color>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer1'
import BgColor from 'common/BgSet'
import OpenScrapyd from './components/OpenScrapyd'

export default {
  name: 'Crawler',
  components: {
    CommonHeader,
    OpenScrapyd,
    CommonFooter,
    BgColor
  }
}

</script>

<style lang="scss" scoped>

</style>
