<template>
  <div class="m-bg">
    <vue-particles color="#dedede" :particleOpacity="0.7" :particlesNumber="80" shapeType="circle" :particleSize="4"
      linesColor="#dedede" :linesWidth="1" :lineLinked="true" :lineOpacity="0.4" :linesDistance="150" :moveSpeed="2"
      :hoverEffect="true" hoverMode="grab" :clickEffect="true" clickMode="push">
    </vue-particles>
    <div class="m-bg-mask m-bg-mask0"></div>
    <div class="m-bg-mask m-bg-mask1"></div>
    <div class="m-bg-mask m-bg-mask2"></div>
    <div class="m-bg-mask m-bg-mask3"></div>
  </div>
</template>

<script>
export default {
  name: 'BgColor'
}

</script>

<style lang='scss' scoped>
  .m-bg {
    position: absolute;
    left: 0;
    top: -400px;
    height: 1000px;
    width: 100%;
    transform: skewY(-11deg);
    background-image: linear-gradient(-20deg, #21d4fd, #b721ff);
    z-index: -1;

    .m-bg-mask {
      position: absolute;
      height: 180px;
    }

    .m-bg-mask0 {
      bottom: 0;
      left: 0;
      width: 30%;
      background-image: linear-gradient(120deg, #6ab3fd, #8ba3fd 102%);
    }

    .m-bg-mask1 {
      bottom: 180px;
      right: 0;
      width: 36%;
      background-image: linear-gradient(120deg, #28c5f5, #6682fe);
    }

    .m-bg-mask2 {
      bottom: 540px;
      left: 0;
      width: 20%;
      height: 240px;
      background-image: linear-gradient(120deg, #8121ff, #5e5ef7);
    }

    .m-bg-mask3 {
      bottom: 540px;
      left: 20%;
      width: 70%;
      height: 240px;
      background-image: linear-gradient(-225deg, #5f2bff, #6088fe 48%, #22ccf6);
    }
  }

</style>
