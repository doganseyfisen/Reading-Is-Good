/**
 * Created CartItem.vue
 */

<template>
    <tr>
        <td><router-link :to="item.book.get_absolute_url">{{ item.book.name }}</router-link></td>
        <td>${{ item.book.price }}</td>
        <td>{{ item.quantity }}
            <a @click="decrementQuantity(item)"><strong>-</strong></a>
            <a @click="incrementQuantity(item)"><strong>+</strong></a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.book.price
        },
        decrementQuantity(item) {
            item.quantity -= 1
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart() {
            this.$emit('removeFromCart', this.item)

            this.updateCart()
        },
    }
}
</script>