import { z } from 'zod';


const usernameValidator = z.string().min(3, 'Username must be at least 3 characters');
const passwordValidator = z.string()
    .min(5, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Must contain uppercase')
    .regex(/[a-z]/, 'Must contain lowercase')
    .regex(/[0-9]/, 'Must contain number');

const urlValidator = z.string()
    .regex(/^(https?:\/\/)?([\w\-])+\.{1}([a-zA-Z]{2,63})([\/\w\-.]*)*\/?$/, 'Invalid URL format')
    .transform((val) => {
        if (!val.startsWith('http://') && !val.startsWith('https://')) {
            return `https://${val}`;
        }
        return val;
    })
    .optional();

const phoneValidator = z.string()
    .regex(/^(\+\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$/, 'Invalid phone number format')
    .transform((val) => {
        // Remove all non-digit characters
        const digits = val.replace(/\D/g, '');
        // Format as (XXX) XXX-XXXX
        if (digits.length === 10) {
            return `(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`;
        }
        // Format with country code +X (XXX) XXX-XXXX
        if (digits.length === 11) {
            return `+${digits[0]} (${digits.slice(1, 4)}) ${digits.slice(4, 7)}-${digits.slice(7)}`;
        }
        return val;
    });

export const loginSchema = z.object({
    username: usernameValidator,
    password: passwordValidator
});

export const registerSchema = loginSchema.extend({
    email: z.email('Invalid email address'),
    firstName: z.string().min(2, 'First name must be at least 2 characters'),
    lastName: z.string().min(2, 'Last name must be at least 2 characters'),
    phoneNumber: phoneValidator.optional(),
    githubUrl: urlValidator,
    linkedinUrl: urlValidator,
    websiteUrl: urlValidator,
});

export type LoginInput = z.infer<typeof loginSchema>;
export type RegisterInput = z.infer<typeof registerSchema>;