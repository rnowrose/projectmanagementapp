<script lang="ts">
    import Card from '$lib/components/base/Card.svelte';
    import EducationInfo from '$lib/components/users/education/EducationInfo.svelte';
    import AdditionalUserInfo from '$lib/components/users/profile/AdditionalUserInfo.svelte';
    import UserProfile from '$lib/components/users/profile/UserProfile.svelte';
    import type { Accomplishments, Education, Experience, User } from '$lib/domain/Users.ts';
    import { userStore } from '$lib/stores/userStore.ts';

    let username = $state<string>('');
    let message = $state<string>('');
    let fullName = $state<string>('');
    let email = $state<string>('');
    let phoneNumber = $state<string>('');
    let educations = $state<Education[]>([]);
    let experiences = $state<Experience[]>([]);
    let accomplishments = $state<Accomplishments[]>([]);
    let password = $state<string>('');
    let summary = $state<string>('');
    let githubUrl = $state<string>('');
    let linkedinUrl = $state<string>('');
    let websiteUrl = $state<string>('');
    let profilePicture = $state<string>('');

    function updateUser(): Promise<void> {
        return userStore.updateUser({
            fullName,
            email,
            phoneNumber,
            username,
            password,
            summary,
            githubUrl,
            linkedinUrl,
            websiteUrl,
            profilePicture,
            education: educations,
            experience: experiences,
            accomplishments: accomplishments
        }).then(() => {
            message = 'Profile updated successfully';
        }).catch((error) => {
            message = 'Failed to update profile';
            console.error('Failed to update profile:', error);
        });
    }

    function deleteEducation(index: number): Promise<void> {
        console.log('Deleting education at index:', index);
        return new Promise((resolve) => {
            educations = educations.filter((_, i) => i !== index);
            resolve();
        });
    }
    
    $effect(() => {
        userStore.profile().then((data: User | null) => {
            if (data) {
                fullName = data.fullName;
                email = data.email;
                phoneNumber = data.phoneNumber || '';
                username = data.username;
                password = data.password || '';
                summary = data.summary || '';
                githubUrl = data.githubUrl || '';
                linkedinUrl = data.linkedinUrl || '';
                websiteUrl = data.websiteUrl || '';
                profilePicture = data.profilePicture || '';
                educations = data.education || [];
                experiences = data.experience || [];
                accomplishments = data.accomplishments || [];
            }
        }).catch((error) => {
            message = 'Failed to load profile';
            console.error('Failed to load profile:', error);
        });
    });
    


</script>
<div class="flex flex-row gap-8">
    <div class="flex flex-col gap-4 mb-4">
        <UserProfile
            {fullName}
            {email}
            {phoneNumber}
            {username}
            {updateUser}
            />
        <AdditionalUserInfo
            githuburl={githubUrl}
            linkedinurl={linkedinUrl}
            websiteurl={websiteUrl}
            {updateUser}
        />
    </div>
    <Card title="Education Information" needsButton={true} buttonName="+">
        {#each educations as education}
            <EducationInfo
                institution={education.institution}
                degree={education.degree}
                fieldOfStudy={education.fieldOfStudy}
                startDate={education.startDate}
                endDate={education.endDate}
                updateEducation={updateUser}
            />
        {/each}
    </Card>
</div>