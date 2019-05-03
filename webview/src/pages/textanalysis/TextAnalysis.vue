<template>
  <div>
    <common-header></common-header>
    <start-analysis></start-analysis>
    <common-footer></common-footer>
    <bg-color></bg-color>
  </div>
</template>

<script>
import CommonHeader from 'common/Header'
import CommonFooter from 'common/Footer'
import BgColor from 'common/BgSet'
import StartAnalysis from './components/StartAnalysis'

export default {
  name: 'TextAnalysis',
  components: {
    CommonHeader,
    StartAnalysis,
    CommonFooter,
    BgColor
  },
  data () {
    return {
      textarea: ''
    }
  }
}

</script>

<style lang="scss" scoped>
</style>
