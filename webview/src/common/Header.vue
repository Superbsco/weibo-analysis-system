<template>
    <div>
        <a href="#" class="head-item">微博用户爬虫</a>
        <a href="#" class="head-item">微博评论爬虫</a>
        <a href="#" class="head-item">微博持续爬虫</a>
        <a href="#" class="head-item">文本情感分析</a>
        <a href="#" class="head-item">爬虫例子</a>
    </div>
</template>

<script>
export default {
    name: 'CommonHeader'
}
</script>

<style lang="scss" scoped>
    div {
        text-align: center;
    }
    a {
        text-decoration: none;
        display: inline-block;
        color: #fff;
        font-size: .3rem;
        padding: .26rem .24rem;
        -webkit-font-smoothing: antialiased;
        text-align: center;
    }
    a:hover {
        color: #4fb6ff;
    }
</style>
