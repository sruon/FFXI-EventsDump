# 17809434 - Magephaud

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 644 bytes      |
| Total Events     | 6              |
| References Count | 29             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [115](#event-115)     | 0x0001       |      9 |              5 |
| [116](#event-116)     | 0x000A       |     84 |             18 |
| [117](#event-117)     | 0x005E       |     12 |              6 |
| [118](#event-118)     | 0x006A       |    141 |             27 |
| [119](#event-119)     | 0x00F7       |    238 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2804      |       10244 |
|       1 | 0x0014      |          20 |
|       2 | 0x2805      |       10245 |
|       3 | 0x2806      |       10246 |
|       4 | 0x2807      |       10247 |
|       5 | 0x2808      |       10248 |
|       6 | 0x2809      |       10249 |
|       7 | 0x280A      |       10250 |
|       8 | 0x280B      |       10251 |
|       9 | 0x280C      |       10252 |
|      10 | 0x280D      |       10253 |
|      11 | 0x280E      |       10254 |
|      12 | 0x280F      |       10255 |
|      13 | 0x2810      |       10256 |
|      14 | 0x2811      |       10257 |
|      15 | 0x2812      |       10258 |
|      16 | 0x00C9      |         201 |
|      17 | 0x0000      |           0 |
|      18 | 0x2813      |       10259 |
|      19 | 0x2814      |       10260 |
|      20 | 0x000A      |          10 |
|      21 | 0x001E      |          30 |
|      22 | 0x0028      |          40 |
|      23 | 0x0032      |          50 |
|      24 | 0x003C      |          60 |
|      25 | 0x0005      |           5 |
|      26 | 0x0050      |          80 |
|      27 | 0x00EE      |         238 |
|      28 | 0x0236      |         566 |

## String References

- **10244**: If ya ever have any problems with those pesky little Tonberries, just come to yer buddy Magephaud. It doesn't look like you're in that much trouble, though.
- **10245**: Heh-heh-heh... You've been out playin' with the Tonberries, haven't ya? Don't try denyin' it. I can tell jus' by lookin' at ya.
- **10246**: I can see them Tonberries' hate fer ya. Now listen close, matey, if ya want t'live.
- **10247**: The little green beasties on this island are all connected. When ya kill one, the others around all get stronger. It's their hate fer ya that drives 'em.
- **10248**: But today's yer lucky day, me matey. I happen t'know a special way of appeasin' those Tonberries.
- **10249**: Har-har-harrr! Ya think I'd tell ya fer free? Bring me three $0. Then I'll let ya in on me little secret.
- **10250**: Bring me three $0. Then I'll let ya in on me little secret. I won't pressure ya into anything if ya think ya can handle the devils on yer own...
- **10251**: One...two...three. Three $0, just like I asked fer. Okay. Let me fill ya in on how to soothe these slimy savages.
- **10252**: Way back when I was still young and didn't know about the hate--the rancor--of the Tonberries, I killed a couple...just like you did.
- **10253**: Then, one day when me and me mateys wuz plunderin' an old temple, I met an old Tonberry who understood the words of men.
- **10254**: It was he who told me of the Tonberries' hate, and that only he could soothe the rancor heaped upon me.
- **10255**: But then he told me t'fork over me gil! That be a beastman fer ya!
- **10256**: So I told him t'show me some evidence before I was handin' over any gil, and with a wave of his wand, he relieved me of the Tonberries' rancor.
- **10257**: And then, did I pay the gil? Of course I didn't! I hit him with a "Sneak Attack" and swiped his key t'the room. Then I used me "Flee" and I was gone like the wind.
- **10258**: Ya get all that? Now ya know what t'do. Here's the key t'that room.
- **10259**: Don't get the wrong idea, now. I only told ya I'd tell you the way t'rid yerself of the rancor, not actually rid ya of it.
- **10260**: You've got the key. What ya do with it is up to you, but watch yer back if yer ever travelin' around that ancient temple.

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

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 07 01 1D 00 80 23  21 00                     ......#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x0107)
  1: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=10244*)
    → "If ya ever have any problems with those pesky little Tonberries, just come to yer buddy Magephaud. It doesn't look like you're in that much trouble, though."
  2: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0008 [0x21] END_EVENT
  4: 0x0009 [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 84 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                42 1A 07 01 66 01            B...f.
0010: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1D 02 80  .........thk1...
0020: 23 1D 03 80 23 1D 04 80  23 66 01 80 F8 FF FF 7F  #...#...#f......
0030: F8 FF FF 7F 74 68 6B 32  53 F8 FF FF 7F F8 FF FF  ....thk2S.......
0040: 7F 74 68 6B 32 1D 05 80  23 66 01 80 F8 FF FF 7F  .thk2...#f......
0050: F8 FF FF 7F 74 6C 6B 30  1D 06 80 23 21 00        ....tlk0...#!.  
```

#### Opcodes

```
  0: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000B [0x1A] CALL_SUBROUTINE(address=0x0107)
  2: 0x000E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  3: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=10245*)
    → "Heh-heh-heh... You've been out playin' with the Tonberries, haven't ya? Don't try denyin' it. I can tell jus' by lookin' at ya."
  4: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=10246*)
    → "I can see them Tonberries' hate fer ya. Now listen close, matey, if ya want t'live."
  6: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=10247*)
    → "The little green beasties on this island are all connected. When ya kill one, the others around all get stronger. It's their hate fer ya that drives 'em."
  8: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0029 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
 10: 0x0038 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 11: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=10248*)
    → "But today's yer lucky day, me matey. I happen t'know a special way of appeasin' those Tonberries."
 12: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 14: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=10249*)
    → "Har-har-harrr! Ya think I'd tell ya fer free? Bring me three $0. Then I'll let ya in on me little secret."
 15: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x005C [0x21] END_EVENT
 17: 0x005D [0x00] END_REQSTACK()
```

### Event 117

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            1A 07                ..
0060: 01 1A 45 01 1D 07 80 23  21 00                    ..E....#!.      
```

#### Opcodes

```
  0: 0x005E [0x1A] CALL_SUBROUTINE(address=0x0107)
  1: 0x0061 [0x1A] CALL_SUBROUTINE(address=0x0145)
  2: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=10250*)
    → "Bring me three $0. Then I'll let ya in on me little secret. I won't pressure ya into anything if ya think ya can handle the devils on yer own..."
  3: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0068 [0x21] END_EVENT
  5: 0x0069 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x006A    |
| Data Size    | 141 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                42 1A 07 01 1D 08            B.....
0070: 80 23 66 01 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B  .#f..........thk
0080: 31 1D 09 80 23 1D 0A 80  23 1D 0B 80 23 1D 0C 80  1...#...#...#...
0090: 23 66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  #f..........thk2
00A0: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 1D 0D 80  S........thk2...
00B0: 23 66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
00C0: 1D 0E 80 23 1D 0F 80 23  66 01 80 F8 FF FF 7F F8  ...#...#f.......
00D0: FF FF 7F 70 61 73 30 53  F8 FF FF 7F F8 FF FF 7F  ...pas0S........
00E0: 70 61 73 30 45 10 80 F0  FF FF 7F F0 FF FF 7F 71  pas0E..........q
00F0: 73 74 63 11 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x006A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006B [0x1A] CALL_SUBROUTINE(address=0x0107)
  2: 0x006E [0x1D] PRINT_EVENT_MESSAGE(message_id=10251*)
    → "One...two...three. Three $0, just like I asked fer. Okay. Let me fill ya in on how to soothe these slimy savages."
  3: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0072 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  5: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=10252*)
    → "Way back when I was still young and didn't know about the hate--the rancor--of the Tonberries, I killed a couple...just like you did."
  6: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=10253*)
    → "Then, one day when me and me mateys wuz plunderin' an old temple, I met an old Tonberry who understood the words of men."
  8: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=10254*)
    → "It was he who told me of the Tonberries' hate, and that only he could soothe the rancor heaped upon me."
 10: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=10255*)
    → "But then he told me t'fork over me gil! That be a beastman fer ya!"
 12: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0091 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
 14: 0x00A0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 15: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=10256*)
    → "So I told him t'show me some evidence before I was handin' over any gil, and with a wave of his wand, he relieved me of the Tonberries' rancor."
 16: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00B1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 18: 0x00C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10257*)
    → "And then, did I pay the gil? Of course I didn't! I hit him with a "Sneak Attack" and swiped his key t'the room. Then I used me "Flee" and I was gone like the wind."
 19: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x00C4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10258*)
    → "Ya get all that? Now ya know what t'do. Here's the key t'that room."
 21: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x00C8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 23: 0x00D7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 24: 0x00E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 25: 0x00F5 [0x21] END_EVENT
 26: 0x00F6 [0x00] END_REQSTACK()
```

### Event 119

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00F7    |
| Data Size    | 238 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      1A  07 01 1A 45 01 1D 12 80         ....E....
0100: 23 1D 13 80 23 21 00 86  00 F8 FF FF 7F 1E F0 FF  #...#!..........
0110: FF 7F 6F 70 1B 66 11 80  F8 FF FF 7F F8 FF FF 7F  ..op.f..........
0120: 74 6C 6B 30 1B 66 11 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0130: 74 6C 6B 31 1B 66 14 80  F8 FF FF 7F F8 FF FF 7F  tlk1.f..........
0140: 74 6C 6B 30 1B 66 01 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0150: 74 6C 6B 30 1B 66 15 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0160: 74 6C 6B 30 1B 66 16 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0170: 74 6C 6B 30 1B 66 17 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0180: 74 6C 6B 30 1B 66 18 80  F8 FF FF 7F F8 FF FF 7F  tlk0.f..........
0190: 74 6C 6B 30 1B 5B 19 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
01A0: 74 6C 6B 30 1B 5B 1A 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
01B0: 74 6C 6B 30 1B 5B 1B 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
01C0: 74 6C 6B 30 1B 5B 1C 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
01D0: 74 6C 6B 30 1B 5B 18 80  F8 FF FF 7F F8 FF FF 7F  tlk0.[..........
01E0: 74 6C 62 30 1B                                    tlb0.           
```

#### Opcodes

```
  0: 0x00F7 [0x1A] CALL_SUBROUTINE(address=0x0107)
  1: 0x00FA [0x1A] CALL_SUBROUTINE(address=0x0145)
  2: 0x00FD [0x1D] PRINT_EVENT_MESSAGE(message_id=10259*)
    → "Don't get the wrong idea, now. I only told ya I'd tell you the way t'rid yerself of the rancor, not actually rid ya of it."
  3: 0x0100 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0101 [0x1D] PRINT_EVENT_MESSAGE(message_id=10260*)
    → "You've got the key. What ya do with it is up to you, but watch yer back if yer ever travelin' around that ancient temple."
  5: 0x0104 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0105 [0x21] END_EVENT
  7: 0x0106 [0x00] END_REQSTACK()

SUBROUTINE_0107:
  8: 0x0107 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  9: 0x010D [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x0112 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0113 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x0114 [0x1B] RETURN

SUBROUTINE_0145:
 13: 0x0145 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 14: 0x0154 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0115 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x0124 [0x1B] RETURN
     0x0125 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x0134 [0x1B] RETURN
     0x0135 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x0144 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x0155 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x0164 [0x1B] RETURN
     0x0165 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x0174 [0x1B] RETURN
     0x0175 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x0184 [0x1B] RETURN
     0x0185 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x0194 [0x1B] RETURN
     0x0195 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x01A4 [0x1B] RETURN
     0x01A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x01B4 [0x1B] RETURN
     0x01B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x01C4 [0x1B] RETURN
     0x01C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x01D4 [0x1B] RETURN
     0x01D5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x01E4 [0x1B] RETURN
```
