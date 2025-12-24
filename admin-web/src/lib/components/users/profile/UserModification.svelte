<script lang="ts">
    interface Props {
        userId?: number;
        firstName: string;
        lastName: string;
        email: string;
        phoneNumber?: string;
        username: string;
        password: string;
        errors: Record<string, string>;
        message?: string;
        modify: () => void;
        modifyButtonText: string;
        isRegister: boolean;
    }

    let { 
        userId = undefined, 
        firstName = $bindable(), 
        lastName = $bindable(), 
        email = $bindable(), 
        phoneNumber = $bindable(''), 
        username = $bindable(), 
        password = $bindable(), 
        errors, 
        message, 
        modify, 
        modifyButtonText, 
        isRegister = false 
    } = $props();</script>


  <form class="fieldset bg-base-200 border-base-300 rounded-box w-100 border p-4" onsubmit={modify}>
      <div class="card w-full">
        <figure class="px-10 pb-2">
          <img src="../admin-cat.png" alt="Register" />
        </figure>
        <div class="divider">{isRegister ? 'Register' : 'Modify User'}</div>
        <div class="card-body">
          {#if message}
            <div role="alert" class="alert alert-error">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>{message}</span>
            </div>
          {/if}

          <label class="label" for="firstName">First Name</label>
          <input 
            id="firstName" 
            type="text" 
            class="input"
            class:input-error={errors.firstName}
            placeholder="First Name" 
            bind:value={firstName} 
          />
          {#if errors.firstName}
            <div class="badge badge-soft badge-error">{errors.firstName}</div>
          {/if}

          <label class="label" for="lastName">Last Name</label>
          <input 
            id="lastName" 
            type="text" 
            class="input"
            class:input-error={errors.lastName}
            placeholder="Last Name" 
            bind:value={lastName} 
          />
          {#if errors.lastName}
            <div class="badge badge-soft badge-error">{errors.lastName}</div>
          {/if}

          <label class="label" for="email">Email</label>
          <input 
            id="email" 
            type="email" 
            class="input"
            class:input-error={errors.email}
            placeholder="email@example.com" 
            bind:value={email} 
          />
          {#if errors.email}
            <div class="badge badge-soft badge-error">{errors.email}</div>
          {/if}

          <label class="label" for="phoneNumber">Phone Number</label>
          <input 
            id="phoneNumber" 
            type="text" 
            class="input"
            class:input-error={errors.phoneNumber}
            placeholder="(123) 456-7890" 
            bind:value={phoneNumber} 
          />
        {#if errors.phoneNumber}
            <div class="badge badge-soft badge-error whitespace-nowrap overflow-hidden text-ellipsis max-w-full">
                {errors.phoneNumber}
            </div>
        {/if}
          <label class="label" for="username">Username</label>
          <input 
            id="username" 
            type="text" 
            class="input"
            class:input-error={errors.username}
            placeholder="Username" 
            bind:value={username} 
          />
          {#if errors.username}
            <div class="badge badge-soft badge-error">{errors.username}</div>
          {/if}

          {#if isRegister}
            <label class="label" for="password">Password</label>
            <input 
              id="password" 
              type="password" 
              class="input"
              class:input-error={errors.password}
              placeholder="Password" 
              bind:value={password} 
            />
            {#if errors.password}
              <div class="badge badge-soft badge-error">{errors.password}</div>
            {/if}
          {/if}
        </div>
        <div class="card-actions justify-center">
          <button class="btn btn-primary" type="submit">{modifyButtonText}</button>
        </div>
      </div>
      {#if isRegister}
        <div class="mt-4 text-center">
            Already have an account?
            <a href="/users/login" class="btn btn-primary btn-xs">Sign in</a>
        </div>
      {/if}
  </form>