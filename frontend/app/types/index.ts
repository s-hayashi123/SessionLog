export interface Member {
  member_id: string;
  name: string;
  age: number;
  gender: "男性" | "女性" | "その他";
  height: number;
  weight: number;
  body_fat: number;
  joined_at: string;
  memo?: string;
}

export interface Session {
  session_date: string;
  duration?: number;
  weight?: number;
  body_fat?: number;
  memo?: string;
}

export interface SessionDetail {
  exercise_id: string;
  sets: number;
  reps: number;
  weight: number;
}
