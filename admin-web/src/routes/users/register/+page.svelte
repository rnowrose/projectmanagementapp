<script lang="ts">
    import { goto } from '$app/navigation';
    import UserModification from '$lib/components/users/profile/UserModification.svelte';
    import { registerSchema } from '$lib/schema/auth.schema.ts';
    import { userStore } from '$lib/stores/userStore.ts';

    let username = $state<string>('');
    let password = $state<string>('');
    let message = $state<string>('');
    let firstName = $state<string>('');
    let lastName = $state<string>('');
    let email = $state<string>('');
    let errors = $state<Record<string, string>>({});
    let phoneNumber = $state<string>('');

    function create() {
        errors = {};
        message = '';

        const result = registerSchema.safeParse({ 
            firstName, lastName, username, email, password 
        });
        
        console.log(result);
        
        if (!result.success) {
            result.error.issues.forEach((issue) => {
                const field = issue.path[0] as string;
                errors[field] = issue.message;
            });
            message = 'Please fix the errors below';
            return;
        }

        userStore.createUser({ 
            username, 
            password, 
            email, 
            phoneNumber,
            fullName: `${firstName} ${lastName}` 
        }).then(() => {
            goto('/users/login');
        }).catch((error) => {
            message = 'Registration failed';
            console.error('Registration failed:', error);
        });
    }
</script>

<div class="min-h-screen flex items-center justify-center">
    <UserModification
        bind:firstName
        bind:lastName
        bind:email
        bind:phoneNumber
        bind:username
        bind:password
        {errors}
        {message}
        modify={create}
        modifyButtonText="Register"
        isRegister={true} 
    />
</div>
