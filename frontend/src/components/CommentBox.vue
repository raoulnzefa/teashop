<template>
<div class="box box-green-prm mb-3 is-flex is-align-items-baseline is-justify-content-space-between">

  <div class="comment-start">
    <span class="is-block comment-owner mr-5">
      <i class="fa-solid fa-user mr-1" style="color: white"></i>{{ comment.owner }} :
    </span>
    <span class="comment-body">{{ comment.body }}</span>
  </div>

  <div class="comment-end">
    <span class="comment-date">{{ comment.created.slice(0,10) }}</span>
  </div>

</div>
</template>

<script>
export default {
  name: "CommentBox",
  props: {
    comment: Object
  }
}
</script>

<style lang="scss" scoped>
$primary-color: #3EB489;
$secondary-color: #92ddc8;

.comment-owner {
  font-size: 1.75rem;
  font-weight: 600;
}

.comment-body {
  font-size: 1.25rem;
  font-weight: 500;
}

.comment-date {
  font-size: 1rem;
  font-weight: 500;
}

</style>