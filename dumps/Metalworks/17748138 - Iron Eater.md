# 17748138 - Iron Eater

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 1616 bytes           |
| Total Events     | 7                    |
| References Count | 35                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [988](#event-988)     | 0x0001       |      1 |              1 |
| [958](#event-958)     | 0x0002       |    745 |             79 |
| [959](#event-959)     | 0x02EB       |     70 |             12 |
| [960](#event-960)     | 0x0331       |    295 |             35 |
| [961](#event-961)     | 0x0458       |     22 |              6 |
| [962](#event-962)     | 0x046E       |    296 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x0127      |         295 |
|       4 | 0xFFFFC473  |  4294952051 |
|       5 | 0x580B      |       22539 |
|       6 | 0xFFFFDBE4  |  4294958052 |
|       7 | 0x0451      |        1105 |
|       8 | 0x018F      |         399 |
|       9 | 0x000F      |          15 |
|      10 | 0x001E      |          30 |
|      11 | 0x2A2E      |       10798 |
|      12 | 0x0045      |          69 |
|      13 | 0x0434      |        1076 |
|      14 | 0x2A2F      |       10799 |
|      15 | 0x2A30      |       10800 |
|      16 | 0x0438      |        1080 |
|      17 | 0x2A31      |       10801 |
|      18 | 0x0007      |           7 |
|      19 | 0x005A      |          90 |
|      20 | 0x2A32      |       10802 |
|      21 | 0x2A33      |       10803 |
|      22 | 0x0436      |        1078 |
|      23 | 0x0437      |        1079 |
|      24 | 0x2A34      |       10804 |
|      25 | 0x2A35      |       10805 |
|      26 | 0x2A36      |       10806 |
|      27 | 0x2A37      |       10807 |
|      28 | 0x2A38      |       10808 |
|      29 | 0x2A39      |       10809 |
|      30 | 0x2A3A      |       10810 |
|      31 | 0x2A3B      |       10811 |
|      32 | 0x2A3C      |       10812 |
|      33 | 0x2A3D      |       10813 |
|      34 | 0x2A3E      |       10814 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 988

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 958

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 745 bytes |
| Instructions | 79        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 45 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64    BE..........fd
0010: 6F 31 01 80 55 00 80 F8  FF FF 7F F8 FF FF 7F 66  o1..U..........f
0020: 64 6F 31 46 01 38 02 80  75 00 03 80 75 01 92 01  do1F.8..u...u...
0030: 0B D0 0E 01 4E 00 F0 FF  FF 7F BA F0 FF FF 7F 04  ....N...........
0040: 80 05 80 06 80 07 80 80  F0 FF FF 7F 80 0B D0 0E  ................
0050: 01 4A F0 FF FF 7F 0B D0  0E 01 45 08 80 F8 FF FF  .J........E.....
0060: 7F F8 FF FF 7F 73 30 37  39 01 80 1C 09 80 45 00  .....s079.....E.
0070: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 55  .........fdi1..U
0080: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 4A 0B  ..........fdi1J.
0090: D0 0E 01 F0 FF FF 7F 1C  0A 80 2B 0B D0 0E 01 0B  ..........+.....
00A0: 80 23 66 0C 80 0B D0 0E  01 0B D0 0E 01 74 6C 6B  .#f..........tlk
00B0: 30 52 08 80 F8 FF FF 7F  F8 FF FF 7F 73 30 37 39  0R..........s079
00C0: 45 08 80 F8 FF FF 7F F8  FF FF 7F 73 30 38 30 01  E..........s080.
00D0: 80 03 02 10 0D 80 2B 0B  D0 0E 01 0E 80 23 45 00  ......+......#E.
00E0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 6F 31 01 80 55  .........fdo1..U
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 31 52 08  ..........fdo1R.
0100: 80 F8 FF FF 7F F8 FF FF  7F 73 30 38 30 6B 69 64  .........s080kid
0110: 6C 30 0B D0 0E 01 66 0C  80 0B D0 0E 01 0B D0 0E  l0....f.........
0120: 01 74 68 6B 31 53 0B D0  0E 01 0B D0 0E 01 74 68  .thk1S........th
0130: 6B 31 45 08 80 F8 FF FF  7F F8 FF FF 7F 73 30 38  k1E..........s08
0140: 31 01 80 1C 09 80 45 00  80 F0 FF FF 7F F0 FF FF  1.....E.........
0150: 7F 66 64 69 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdi1..U........
0160: FF 7F 66 64 69 31 2B 0B  D0 0E 01 0F 80 23 52 08  ..fdi1+......#R.
0170: 80 F8 FF FF 7F F8 FF FF  7F 73 30 38 31 45 08 80  .........s081E..
0180: F8 FF FF 7F F8 FF FF 7F  73 30 38 32 01 80 66 0C  ........s082..f.
0190: 80 0B D0 0E 01 0B D0 0E  01 74 68 6B 32 03 02 10  .........thk2...
01A0: 10 80 2B 0B D0 0E 01 11  80 23 6E F0 FF FF 7F 12  ..+......#n.....
01B0: 80 99 F0 FF FF 7F 1C 13  80 52 08 80 F8 FF FF 7F  .........R......
01C0: F8 FF FF 7F 73 30 38 32  45 08 80 F8 FF FF 7F F8  ....s082E.......
01D0: FF FF 7F 73 30 38 33 01  80 66 0C 80 0B D0 0E 01  ...s083..f......
01E0: 0B D0 0E 01 74 6C 6B 30  2B 0B D0 0E 01 14 80 23  ....tlk0+......#
01F0: 66 0C 80 0B D0 0E 01 0B  D0 0E 01 74 6C 6B 31 52  f..........tlk1R
0200: 08 80 F8 FF FF 7F F8 FF  FF 7F 73 30 38 33 45 08  ..........s083E.
0210: 80 F8 FF FF 7F F8 FF FF  7F 73 30 38 34 01 80 2B  .........s084..+
0220: 0B D0 0E 01 15 80 23 52  08 80 F8 FF FF 7F F8 FF  ......#R........
0230: FF 7F 73 30 38 34 45 08  80 F8 FF FF 7F F8 FF FF  ..s084E.........
0240: 7F 73 30 38 35 01 80 66  0C 80 0B D0 0E 01 0B D0  .s085..f........
0250: 0E 01 74 6C 6B 30 03 02  10 16 80 03 03 10 17 80  ..tlk0..........
0260: 2B 0B D0 0E 01 18 80 23  2B 0B D0 0E 01 19 80 23  +......#+......#
0270: 52 08 80 F8 FF FF 7F F8  FF FF 7F 73 30 38 35 45  R..........s085E
0280: 08 80 F8 FF FF 7F F8 FF  FF 7F 73 30 38 36 01 80  ..........s086..
0290: 66 0C 80 0B D0 0E 01 0B  D0 0E 01 74 6C 6B 31 2B  f..........tlk1+
02A0: 0B D0 0E 01 1A 80 23 45  00 80 F8 FF FF 7F F8 FF  ......#E........
02B0: FF 7F 66 64 6F 31 01 80  55 00 80 F8 FF FF 7F F8  ..fdo1..U.......
02C0: FF FF 7F 66 64 6F 31 52  08 80 F8 FF FF 7F F8 FF  ...fdo1R........
02D0: FF 7F 73 30 38 36 46 00  45 00 80 F0 FF FF 7F F0  ..s086F.E.......
02E0: FF FF 7F 66 64 69 32 01  80 21 00                 ...fdi2..!.     
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0014 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0023 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0025 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0028 [0x75] LOAD_ROOM(Load indoor room, room=295*)
  6: 0x002C [0x75] LOAD_ROOM(No action)
  7: 0x002E [0x92] Striking Snake (ID: 17747979/0x010ED00B)->Render.Flags3 ^= 0x01
  8: 0x0034 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
  9: 0x003A [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-15.245*, pos_z=22.539*, pos_y=-9.244*, direction=97.1°*)
 10: 0x0047 [0x80] LOAD_WAIT(entity=LocalPlayer)
 11: 0x004C [0x80] LOAD_WAIT(entity=Striking Snake (ID: 17747979/0x010ED00B))
 12: 0x0051 [0x4A] LocalPlayer looks at Striking Snake (ID: 17747979/0x010ED00B)
 13: 0x005A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s079" with entities [EventEntity, EventEntity], work=[399*, 0*]
 14: 0x006B [0x1C] WAIT(15* ticks)
 15: 0x006E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x007F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x008E [0x4A] Striking Snake (ID: 17747979/0x010ED00B) looks at LocalPlayer
 18: 0x0097 [0x1C] WAIT(30* ticks)
 19: 0x009A [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10798*]:
    → "Yes? You need something? I've no time for idle chitchat."
 20: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00A2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 22: 0x00B1 [0x52] END_LOAD_SCHEDULER: End scheduler "s079" with entities [EventEntity, EventEntity], work=399*
 23: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s080" with entities [EventEntity, EventEntity], work=[399*, 0*]
 24: 0x00D1 [0x03] Work_Zone[2] = 1076*
 25: 0x00D6 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10799*]:
    → "Son of a hexagun! Are those $5? What in the Goddess's name are you doing with those?"
 26: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 28: 0x00EF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 29: 0x00FE [0x52] END_LOAD_SCHEDULER: End scheduler "s080" with entities [EventEntity, EventEntity], work=399*
 30: 0x010D [0x6B] STOP_AND_IDLE: Striking Snake (ID: 17747979/0x010ED00B) stops current action and resets to idle (animation="idl0")
 31: 0x0116 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 32: 0x0125 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)]
 33: 0x0132 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s081" with entities [EventEntity, EventEntity], work=[399*, 0*]
 34: 0x0143 [0x1C] WAIT(15* ticks)
 35: 0x0146 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x0157 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 37: 0x0166 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10800*]:
    → "I see, I see. Bullets to blast through magic armor, you say?"
 38: 0x016D [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x016E [0x52] END_LOAD_SCHEDULER: End scheduler "s081" with entities [EventEntity, EventEntity], work=399*
 40: 0x017D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s082" with entities [EventEntity, EventEntity], work=[399*, 0*]
 41: 0x018E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 42: 0x019D [0x03] Work_Zone[2] = 1080*
 43: 0x01A2 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10801*]:
    → "You wouldn't happen to be lookin' for something like the old $5 they used back in the Great War, would you?"
 44: 0x01A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x01AA [0x6E] LocalPlayer uses emote 7*
 46: 0x01B1 [0x99] Wait for LocalPlayer animation to complete
 47: 0x01B6 [0x1C] WAIT(90* ticks)
 48: 0x01B9 [0x52] END_LOAD_SCHEDULER: End scheduler "s082" with entities [EventEntity, EventEntity], work=399*
 49: 0x01C8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s083" with entities [EventEntity, EventEntity], work=[399*, 0*]
 50: 0x01D9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 51: 0x01E8 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10802*]:
    → "Ahh...stirs up memories in this old Galka's soul, it does. After the war ended, I never thought I'd hear the name again."
 52: 0x01EF [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x01F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 54: 0x01FF [0x52] END_LOAD_SCHEDULER: End scheduler "s083" with entities [EventEntity, EventEntity], work=399*
 55: 0x020E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [EventEntity, EventEntity], work=[399*, 0*]
 56: 0x021F [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10803*]:
    → "Goddess only knows what you'd want with those old things...but yes, I think I could do it for you. There's just one catch. The casting process requires some rather...rare...ingredients."
 57: 0x0226 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x0227 [0x52] END_LOAD_SCHEDULER: End scheduler "s084" with entities [EventEntity, EventEntity], work=399*
 59: 0x0236 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s085" with entities [EventEntity, EventEntity], work=[399*, 0*]
 60: 0x0247 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 61: 0x0256 [0x03] Work_Zone[2] = 1078*
 62: 0x025B [0x03] Work_Zone[3] = 1079*
 63: 0x0260 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10804*]:
    → "3 and $3, to be exact."
 64: 0x0267 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0268 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10805*]:
    → "Provide me with what I need, and the job is as good as done."
 66: 0x026F [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x0270 [0x52] END_LOAD_SCHEDULER: End scheduler "s085" with entities [EventEntity, EventEntity], work=399*
 68: 0x027F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s086" with entities [EventEntity, EventEntity], work=[399*, 0*]
 69: 0x0290 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 70: 0x029F [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10806*]:
    → "Where to find them, you ask? I haven't a clue. They say there was once a plentiful supply in North Gustaberg, but it was exhausted completely by the war's end..."
 71: 0x02A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 72: 0x02A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 73: 0x02B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 74: 0x02C7 [0x52] END_LOAD_SCHEDULER: End scheduler "s086" with entities [EventEntity, EventEntity], work=399*
 75: 0x02D6 [0x46] CAMERA_CONTROL: Restore default settings
 76: 0x02D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 77: 0x02E9 [0x21] END_EVENT
 78: 0x02EA [0x00] END_REQSTACK()
```

### Event 959

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02EB   |
| Data Size    | 70 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:                                   4A 0B D0 0E 01             J....
02F0: F0 FF FF 7F 1C 0A 80 66  0C 80 0B D0 0E 01 0B D0  .......f........
0300: 0E 01 74 6C 6B 30 03 02  10 16 80 03 03 10 17 80  ..tlk0..........
0310: 2B 0B D0 0E 01 1B 80 23  66 0C 80 0B D0 0E 01 0B  +......#f.......
0320: D0 0E 01 74 6C 6B 31 2B  0B D0 0E 01 1C 80 23 21  ...tlk1+......#!
0330: 00                                                .               
```

#### Opcodes

```
  0: 0x02EB [0x4A] Striking Snake (ID: 17747979/0x010ED00B) looks at LocalPlayer
  1: 0x02F4 [0x1C] WAIT(30* ticks)
  2: 0x02F7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
  3: 0x0306 [0x03] Work_Zone[2] = 1078*
  4: 0x030B [0x03] Work_Zone[3] = 1079*
  5: 0x0310 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10807*]:
    → "Provide me with the materials I need, and your job is as good as done."
  6: 0x0317 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0318 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
  8: 0x0327 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10808*]:
    → "Where to find them...? I haven't a clue. I hear they used to be plentiful in North Gustaberg, but the supply was surely exhausted years ago..."
  9: 0x032E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x032F [0x21] END_EVENT
 11: 0x0330 [0x00] END_REQSTACK()
```

### Event 960

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0331    |
| Data Size    | 295 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0330:    42 45 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F   BE..........fdo
0340: 31 01 80 55 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U..........fd
0350: 6F 31 46 01 38 02 80 75  00 03 80 75 01 92 01 0B  o1F.8..u...u....
0360: D0 0E 01 4E 00 F0 FF FF  7F BA F0 FF FF 7F 04 80  ...N............
0370: 05 80 06 80 07 80 80 F0  FF FF 7F 80 0B D0 0E 01  ................
0380: 4A F0 FF FF 7F 0B D0 0E  01 4A 0B D0 0E 01 F0 FF  J........J......
0390: FF 7F 1C 0A 80 45 08 80  F8 FF FF 7F F8 FF FF 7F  .....E..........
03A0: 73 30 38 37 01 80 1C 09  80 45 00 80 F0 FF FF 7F  s087.....E......
03B0: F0 FF FF 7F 66 64 69 31  01 80 55 00 80 F0 FF FF  ....fdi1..U.....
03C0: 7F F0 FF FF 7F 66 64 69  31 6E 0B D0 0E 01 12 80  .....fdi1n......
03D0: 99 0B D0 0E 01 2B 0B D0  0E 01 1D 80 23 52 08 80  .....+......#R..
03E0: F8 FF FF 7F F8 FF FF 7F  73 30 38 37 45 08 80 F8  ........s087E...
03F0: FF FF 7F F8 FF FF 7F 73  30 38 38 01 80 66 0C 80  .......s088..f..
0400: 0B D0 0E 01 0B D0 0E 01  74 6C 6B 30 2B 0B D0 0E  ........tlk0+...
0410: 01 1E 80 23 45 00 80 F8  FF FF 7F F8 FF FF 7F 66  ...#E..........f
0420: 64 6F 31 01 80 55 00 80  F8 FF FF 7F F8 FF FF 7F  do1..U..........
0430: 66 64 6F 31 52 08 80 F8  FF FF 7F F8 FF FF 7F 73  fdo1R..........s
0440: 30 38 38 46 00 45 00 80  F0 FF FF 7F F0 FF FF 7F  088F.E..........
0450: 66 64 69 32 01 80 21 00                           fdi2..!.        
```

#### Opcodes

```
  0: 0x0331 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0332 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0343 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x0352 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0354 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0357 [0x75] LOAD_ROOM(Load indoor room, room=295*)
  6: 0x035B [0x75] LOAD_ROOM(No action)
  7: 0x035D [0x92] Striking Snake (ID: 17747979/0x010ED00B)->Render.Flags3 ^= 0x01
  8: 0x0363 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
  9: 0x0369 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-15.245*, pos_z=22.539*, pos_y=-9.244*, direction=97.1°*)
 10: 0x0376 [0x80] LOAD_WAIT(entity=LocalPlayer)
 11: 0x037B [0x80] LOAD_WAIT(entity=Striking Snake (ID: 17747979/0x010ED00B))
 12: 0x0380 [0x4A] LocalPlayer looks at Striking Snake (ID: 17747979/0x010ED00B)
 13: 0x0389 [0x4A] Striking Snake (ID: 17747979/0x010ED00B) looks at LocalPlayer
 14: 0x0392 [0x1C] WAIT(30* ticks)
 15: 0x0395 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s087" with entities [EventEntity, EventEntity], work=[399*, 0*]
 16: 0x03A6 [0x1C] WAIT(15* ticks)
 17: 0x03A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x03BA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 19: 0x03C9 [0x6E] Striking Snake (ID: 17747979/0x010ED00B) uses emote 7*
 20: 0x03D0 [0x99] Wait for Striking Snake (ID: 17747979/0x010ED00B) animation to complete
 21: 0x03D5 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10809*]:
    → "Oh ho, well look at this! It seems I underestimated you. Well, a promise is a promise...one order of beastman-blasting bullets, coming right up!"
 22: 0x03DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x03DD [0x52] END_LOAD_SCHEDULER: End scheduler "s087" with entities [EventEntity, EventEntity], work=399*
 24: 0x03EC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s088" with entities [EventEntity, EventEntity], work=[399*, 0*]
 25: 0x03FD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 26: 0x040C [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10810*]:
    → "Good craftsmanship takes time, but I'll be done before you know it. Why don't you head to the Markets and try to catch yourself a gold carp or two while you wait?"
 27: 0x0413 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0414 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 29: 0x0425 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 30: 0x0434 [0x52] END_LOAD_SCHEDULER: End scheduler "s088" with entities [EventEntity, EventEntity], work=399*
 31: 0x0443 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x0445 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 33: 0x0456 [0x21] END_EVENT
 34: 0x0457 [0x00] END_REQSTACK()
```

### Event 961

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0458   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0450:                          4A 0B D0 0E 01 F0 FF FF          J.......
0460: 7F 1C 0A 80 2B 0B D0 0E  01 1F 80 23 21 00        ....+......#!.  
```

#### Opcodes

```
  0: 0x0458 [0x4A] Striking Snake (ID: 17747979/0x010ED00B) looks at LocalPlayer
  1: 0x0461 [0x1C] WAIT(30* ticks)
  2: 0x0464 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10811*]:
    → "Don't you know better than to rush a master at work? Just a bit longer, I say!"
  3: 0x046B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x046C [0x21] END_EVENT
  5: 0x046D [0x00] END_REQSTACK()
```

### Event 962

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x046E    |
| Data Size    | 296 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0460:                                            42 45                BE
0470: 00 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
0480: 55 00 80 F8 FF FF 7F F8  FF FF 7F 66 64 6F 31 46  U..........fdo1F
0490: 01 38 02 80 75 00 03 80  75 01 92 01 0B D0 0E 01  .8..u...u.......
04A0: 4E 00 F0 FF FF 7F BA F0  FF FF 7F 04 80 05 80 06  N...............
04B0: 80 07 80 80 F0 FF FF 7F  80 0B D0 0E 01 4A F0 FF  .............J..
04C0: FF 7F 0B D0 0E 01 4A 0B  D0 0E 01 F0 FF FF 7F 1C  ......J.........
04D0: 0A 80 45 08 80 F8 FF FF  7F F8 FF FF 7F 73 30 38  ..E..........s08
04E0: 39 01 80 1C 09 80 45 00  80 F0 FF FF 7F F0 FF FF  9.....E.........
04F0: 7F 66 64 69 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdi1..U........
0500: FF 7F 66 64 69 31 66 0C  80 0B D0 0E 01 0B D0 0E  ..fdi1f.........
0510: 01 74 6C 6B 30 03 02 10  10 80 2B 0B D0 0E 01 20  .tlk0.....+.... 
0520: 80 23 2B 0B D0 0E 01 21  80 23 52 08 80 F8 FF FF  .#+....!.#R.....
0530: 7F F8 FF FF 7F 73 30 38  39 45 08 80 F8 FF FF 7F  .....s089E......
0540: F8 FF FF 7F 73 30 39 30  01 80 2B 0B D0 0E 01 22  ....s090..+...."
0550: 80 23 45 00 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  .#E..........fdo
0560: 31 01 80 55 00 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U..........fd
0570: 6F 31 52 08 80 F8 FF FF  7F F8 FF FF 7F 73 30 39  o1R..........s09
0580: 30 46 00 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0F.E..........fd
0590: 69 32 01 80 21 00                                 i2..!.          
```

#### Opcodes

```
  0: 0x046E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x046F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  2: 0x0480 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
  3: 0x048F [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0491 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0494 [0x75] LOAD_ROOM(Load indoor room, room=295*)
  6: 0x0498 [0x75] LOAD_ROOM(No action)
  7: 0x049A [0x92] Striking Snake (ID: 17747979/0x010ED00B)->Render.Flags3 ^= 0x01
  8: 0x04A0 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
  9: 0x04A6 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-15.245*, pos_z=22.539*, pos_y=-9.244*, direction=97.1°*)
 10: 0x04B3 [0x80] LOAD_WAIT(entity=LocalPlayer)
 11: 0x04B8 [0x80] LOAD_WAIT(entity=Striking Snake (ID: 17747979/0x010ED00B))
 12: 0x04BD [0x4A] LocalPlayer looks at Striking Snake (ID: 17747979/0x010ED00B)
 13: 0x04C6 [0x4A] Striking Snake (ID: 17747979/0x010ED00B) looks at LocalPlayer
 14: 0x04CF [0x1C] WAIT(30* ticks)
 15: 0x04D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s089" with entities [EventEntity, EventEntity], work=[399*, 0*]
 16: 0x04E3 [0x1C] WAIT(15* ticks)
 17: 0x04E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x04F7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 19: 0x0506 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Striking Snake (ID: 17747979/0x010ED00B), Striking Snake (ID: 17747979/0x010ED00B)], work=69*
 20: 0x0515 [0x03] Work_Zone[2] = 1080*
 21: 0x051A [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10812*]:
    → "I was wondering when you'd come back. Here you are, one order of $5, just like we used to make 'em!"
 22: 0x0521 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0522 [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10813*]:
    → "I even took the liberty of making a few improvements to the old recipe. One blast from these and even the most potent magical armor will be reduced to little more than scrap metal."
 24: 0x0529 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x052A [0x52] END_LOAD_SCHEDULER: End scheduler "s089" with entities [EventEntity, EventEntity], work=399*
 26: 0x0539 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s090" with entities [EventEntity, EventEntity], work=[399*, 0*]
 27: 0x054A [0x2B] Striking Snake (ID: 17747979/0x010ED00B) [10814*]:
    → "My fee? Hah! Don't mention it! I haven't enjoyed my work this much in years. If you come across any other curiosities, you know where to find me!"
 28: 0x0551 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0552 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 30: 0x0563 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 31: 0x0572 [0x52] END_LOAD_SCHEDULER: End scheduler "s090" with entities [EventEntity, EventEntity], work=399*
 32: 0x0581 [0x46] CAMERA_CONTROL: Restore default settings
 33: 0x0583 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x0594 [0x21] END_EVENT
 35: 0x0595 [0x00] END_REQSTACK()
```
