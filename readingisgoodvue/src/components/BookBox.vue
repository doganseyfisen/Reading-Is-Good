/**
 * Created BookBox.vue   
 */
 
<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="book.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ book.name }}</h3>
            <p class="is-size-6 hast-text-grey">${{ book.price }} <em>(Stock: {{ book.stock }})</em></p>

            <router-link v-bind:to="book.get_absolute_url" class="button is-dark mt-4">For details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BookBox',
    props: {
        book: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>