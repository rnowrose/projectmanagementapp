<script lang="ts">
    import { userStore } from '$lib/stores/userStore.ts';
    import Modal from '$lib/components/base/Modal.svelte';
    import UserModification from './UserModification.svelte';

    interface Props {
        fullName: string;
        email: string;
        phoneNumber?: string;
        username: string;
        updateUser: () => Promise<void>;
    }
    let { fullName, email, phoneNumber = '', username, updateUser } = $props();
    let errors = $state<Record<string, string>>({});
    let message = $state<string>('');
    let firstName = $derived(fullName.split(' ')[0] || '');
    let lastName = $derived(fullName.split(' ')[1] || '');
    


</script>
<Modal title="Update User Profile">
    <UserModification
        bind:firstName
        bind:lastName
        bind:email
        bind:phoneNumber
        bind:username
        {errors}
        {message}
        modifyButtonText="Update Profile"
        isRegister={false}
        modify={updateUser}
    />
</Modal>