<script lang="ts">
    import EditDeleteCard from '$lib/components/base/EditDeleteCard.svelte';
    import UpsertEducation from './UpsertEducation.svelte';

    interface Props {
        institution: string;
        degree: string;
        fieldOfStudy: string;
        startDate: string;
        endDate?: string;
        deleteEducation: () => Promise<void>;
        updateEducation: () => Promise<void>;
    }
    let { institution, degree, fieldOfStudy, startDate, endDate = '', updateEducation, deleteEducation } = $props();
    let updateEducationModal = $state<HTMLDialogElement | null>(null);
</script>
<EditDeleteCard 
    title="Education Information" 
    editModal={updateEducation} 
    deleteData={deleteEducation}
>
    <p><strong>Institution:</strong> {institution}</p>
    <p><strong>Degree:</strong> {degree}</p>
    <p><strong>Field of Study:</strong> {fieldOfStudy}</p>
    <p><strong>Start Date:</strong> {startDate}</p>
    {#if endDate}
        <p><strong>End Date:</strong> {endDate}</p>
    {/if}

    <button class="btn btn-primary" onclick={() => updateEducationModal.showModal()}>Edit</button>
    <dialog bind:this={updateEducationModal} id="update_education" class="modal">
        <UpsertEducation
            {institution}
            {degree}
            {fieldOfStudy}
            {startDate}
            {endDate}
            {updateEducation}
        />
    </dialog>
</EditDeleteCard>