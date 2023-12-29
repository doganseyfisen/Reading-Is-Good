/**
 * Created Book.vue 
 */

<template>
    <div class="page-book">
        <div class="columns is-multiline">
            <div class="column is-3">
                <h1 class="title">{{ book.name }}</h1>
                <figure class="image mb-6">
                    <img v-bind:src="book.get_image">
                </figure>
            </div>

            <div class="column is-4">
                <h2 clas="subtitle">Book Information</h2>
                <p><strong>Price: </strong>${{ book.price }}</p>
                <div class="field has-addons mt-4">
                    <div>
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Book',
    data() {
        return {
            book: {},
            quantity: 1
        }
    },
    mounted() {
        this.getBook()
    },
    methods: {
        /**
         * Make sure that you don't call 'false' before it's finished (async).
         * 
         */
        async getBook() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const book_slug = this.$route.params.book_slug
            /**
             * Axios
             */
            await axios
                /**
                 * Used `` instead of "" or ''
                 */
                .get(`/api/v1/books/${category_slug}/${book_slug}`)
                .then(response => {
                    this.book = response.data

                    document.title = this.book.name + ' | Reading Is Good'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                book: this.book,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The book was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>