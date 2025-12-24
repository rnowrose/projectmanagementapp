<script lang="ts">
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';
    import { userStore } from '$lib/stores/userStore';
    import NavBar from '$lib/components/base/NavBar.svelte';
    import SideBar from '$lib/components/base/SideBar.svelte';
    import '$lib/style/layout.css';
    import { onMount } from 'svelte';
    
    let { children } = $props();
    
    let isAuthPage = $derived($page.url.pathname === '/users/login' || $page.url.pathname === '/users/register');

    onMount(() => {
        if (!$userStore.isAuthenticated && !userStore.loginInfo) {
            goto('/users/login');
        }
    });

</script>
{#if isAuthPage}
    <!-- Login/Register pages without NavBar/SideBar -->
    {@render children()}
{:else if $userStore.isAuthenticated}
    <!-- Authenticated pages with layout -->
    <div class="min-h-screen bg-background">
        <NavBar />
         <div class="flex">
            <SideBar />
            <main class="flex-1 mx-40 my-4 p-4">
                {@render children()}
            </main>
        </div>
    </div>
{:else}
    <!-- Loading or redirecting -->
    <div class="min-h-screen flex items-center justify-center">
        <span class="loading loading-spinner loading-lg"></span>
    </div>
{/if}

