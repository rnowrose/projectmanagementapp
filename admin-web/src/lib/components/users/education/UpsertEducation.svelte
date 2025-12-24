<script lang="ts">
    import Modal from "$lib/components/base/Modal.svelte";

     interface Props {
        institution: string;
        degree: string;
        fieldOfStudy: string;
        startDate: string;
        endDate?: string;
        updateEducation: () => Promise<void>;
    }
    let { institution, degree, fieldOfStudy, startDate, endDate = '', updateEducation } = $props();
</script>

<Modal title="Update Education Information">
    <form class="flex flex-col gap-4 p-4" onsubmit={updateEducation}>
        <div class="form-control w-full">
            <label class="label">
                <span class="label-text">Institution</span>
            </label>
            <input
                type="text"
                class="input w-full"
                placeholder="Institution"
                bind:value={institution}            
                required
            />      
        </div>
        <div class="form-control w-full">
            <label class="label">
                <span class="label-text">Degree</span>
            </label>
            <input
                type="text"
                class="input w-full"
                placeholder="Degree"
                bind:value={degree}            
                required
            />      
        </div>
        <div class="form-control w-full">
            <label class="label">
                <span class="label-text">Field of Study</span>
            </label>
            <input
                type="text"
                class="input w-full"
                placeholder="Field of Study"
                bind:value={fieldOfStudy}            
                required
            />      
        </div>
        <div class="form-control w-full">
            <label class="label">
                <span class="label-text">Start Date</span>
            </label>
            <input
                type="date"
                class="input w-full"
                placeholder="Start Date"
                bind:value={startDate}            
                required
            />      
        </div>
        <div class="form-control w-full">
            <label class="label">
                <span class="label-text">End Date</span>
            </label>
            <input
                type="date"
                class="input w-full"
                placeholder="End Date"
                bind:value={endDate}            
            />      
        </div>
        <div class="modal-action">
            <button class="btn btn-primary" type="submit">Save</button>
        </div>
    </form>
</Modal>
