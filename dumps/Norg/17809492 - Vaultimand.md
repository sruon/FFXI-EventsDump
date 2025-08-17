# 17809492 - Vaultimand

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 616 bytes      |
| Total Events     | 10             |
| References Count | 32             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |     20 |             10 |
| [101](#event-101)     | 0x0015       |     63 |             13 |
| [102](#event-102)     | 0x0054       |     13 |              7 |
| [103](#event-103)     | 0x0061       |     16 |              8 |
| [104](#event-104)     | 0x0071       |     13 |              7 |
| [105](#event-105)     | 0x007E       |     13 |              7 |
| [106](#event-106)     | 0x008B       |     20 |             10 |
| [107](#event-107)     | 0x009F       |      9 |              5 |
| [108](#event-108)     | 0x00A8       |    263 |             40 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28B0      |       10416 |
|       1 | 0x28B1      |       10417 |
|       2 | 0x28B2      |       10418 |
|       3 | 0x0014      |          20 |
|       4 | 0x28B3      |       10419 |
|       5 | 0x28B4      |       10420 |
|       6 | 0x28B5      |       10421 |
|       7 | 0x28B6      |       10422 |
|       8 | 0x28B7      |       10423 |
|       9 | 0x28B8      |       10424 |
|      10 | 0x28B9      |       10425 |
|      11 | 0x28BA      |       10426 |
|      12 | 0x28BB      |       10427 |
|      13 | 0x28BC      |       10428 |
|      14 | 0x28BD      |       10429 |
|      15 | 0x28BE      |       10430 |
|      16 | 0x28BF      |       10431 |
|      17 | 0x28C0      |       10432 |
|      18 | 0x28C1      |       10433 |
|      19 | 0x28C2      |       10434 |
|      20 | 0x0015      |          21 |
|      21 | 0x28C3      |       10435 |
|      22 | 0x0000      |           0 |
|      23 | 0x000A      |          10 |
|      24 | 0x001E      |          30 |
|      25 | 0x0028      |          40 |
|      26 | 0x0032      |          50 |
|      27 | 0x003C      |          60 |
|      28 | 0x0005      |           5 |
|      29 | 0x0050      |          80 |
|      30 | 0x00EE      |         238 |
|      31 | 0x0236      |         566 |

## String References

- **10416**: Who tha hell are you? <Player>? Never heard of ya. How am I supposed to remember the name of one puny ant when there's millions of ya swarmin' around?
- **10417**: Do a little work around here, and there might be somebody that'll remember your ugly face...no guarantees, though.
- **10418**: Ya gotta get people t'trust ya. Once people do, you'll start makin' a name fer yerself 'round here.
- **10419**: <Player>? I mighta hearda somebody that went by that name, but I meets a lot of people in me line of work.
- **10420**: Don't look so upset there, matey. It takes a lot t'get people t'remember ya. It all starts with trust!
- **10421**: Yer an adventurer, go an' help people out. Little by little, they'll begin t'trust ya, but don't expect anythin' right away.
- **10422**: Wait a minute, I remember you...Mich...no...<Player>, right?
- **10423**: Ya see, do a little work, and people start recognizin' ya. Keep up tha good work!
- **10424**: Well, if it isn't <Player>. Hear yer name lots 'round these parts lately. Why, I remembers when you was nothin' but a measly insect.
- **10425**: Thanks t'me advice, you're doin' quite well here in Norg.
- **10426**: Oh, <Player>. I was just talkin' to me mateys about ya the other day.
- **10427**: Nothin' bad, of course. They had all heard about yer deeds fer Norg. Some are even startin' t'think that maybe all you adventurers ain't so bad after all.
- **10428**: <Player>! There's hardly a soul in Norg that doesn't know yer bloody name.
- **10429**: Oh, sorry 'bout that. Me mum never did teach me no manners. I'll watch me damn mouth...I mean, I'll watch me mouth from now on.
- **10430**: <Player>...[Mister/Miss] <Player>. You've become quite the household name 'round Norg.
- **10431**: All me mateys keep askin' me if I can introduce them to ya. You've made quite a reputation for yerself!
- **10432**: Lookin' at ya gets me thinkin' like I should leave tha life on the open sea, and become an adventurer!
- **10433**: [Mister/Miss] <Player>! There's already rumors of yer last adventure goin' 'round Norg. You're startin' t'become some sorta legend!
- **10434**: [Lord/Lady] <Player>! Next t'our leader, Gilgamesh, yer the most famous person in all'a Norg! Some of me mateys are even callin' ya a hero!
- **10435**: May the light of the Dawn Goddess shine down upon ya in all yer journeys 'round Vana'diel!

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

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A D1 00 1D 00 80 23  1A 0F 01 1D 01 80 23 1D   ......#......#.
0010: 02 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=10416*)
    → "Who tha hell are you? <Player>? Never heard of ya. How am I supposed to remember the name of one puny ant when there's millions of ya swarmin' around?"
  2: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0008 [0x1A] CALL_SUBROUTINE(address=0x010F)
  4: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=10417*)
    → "Do a little work around here, and there might be somebody that'll remember your ugly face...no guarantees, though."
  5: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=10418*)
    → "Ya gotta get people t'trust ya. Once people do, you'll start makin' a name fer yerself 'round here."
  7: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0013 [0x21] END_EVENT
  9: 0x0014 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 63 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1A D1 00  66 03 80 F8 FF FF 7F F8       ...f.......
0020: FF FF 7F 74 68 6B 31 1D  04 80 23 66 03 80 F8 FF  ...thk1...#f....
0030: FF 7F F8 FF FF 7F 74 68  6B 32 53 F8 FF FF 7F F8  ......thk2S.....
0040: FF FF 7F 74 68 6B 32 1A  0F 01 1D 05 80 23 1D 06  ...thk2......#..
0050: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0015 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0018 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  2: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=10419*)
    → "<Player>? I mighta hearda somebody that went by that name, but I meets a lot of people in me line of work."
  3: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  5: 0x003A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  6: 0x0047 [0x1A] CALL_SUBROUTINE(address=0x010F)
  7: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=10420*)
    → "Don't look so upset there, matey. It takes a lot t'get people t'remember ya. It all starts with trust!"
  8: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=10421*)
    → "Yer an adventurer, go an' help people out. Little by little, they'll begin t'trust ya, but don't expect anythin' right away."
 10: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0052 [0x21] END_EVENT
 12: 0x0053 [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             1A D1 00 1D  07 80 23 1D 08 80 23 21      ......#...#!
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0054 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=10422*)
    → "Wait a minute, I remember you...Mich...no...<Player>, right?"
  2: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=10423*)
    → "Ya see, do a little work, and people start recognizin' ya. Keep up tha good work!"
  4: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x005F [0x21] END_EVENT
  6: 0x0060 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    1A D1 00 1A 0F 01 1D  09 80 23 1D 0A 80 23 21   .........#...#!
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0061 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0064 [0x1A] CALL_SUBROUTINE(address=0x010F)
  2: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=10424*)
    → "Well, if it isn't <Player>. Hear yer name lots 'round these parts lately. Why, I remembers when you was nothin' but a measly insect."
  3: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=10425*)
    → "Thanks t'me advice, you're doin' quite well here in Norg."
  5: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006F [0x21] END_EVENT
  7: 0x0070 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    1A D1 00 1D 0B 80 23  1D 0C 80 23 21 00         ......#...#!.  
```

#### Opcodes

```
  0: 0x0071 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=10426*)
    → "Oh, <Player>. I was just talkin' to me mateys about ya the other day."
  2: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=10427*)
    → "Nothin' bad, of course. They had all heard about yer deeds fer Norg. Some are even startin' t'think that maybe all you adventurers ain't so bad after all."
  4: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x007C [0x21] END_EVENT
  6: 0x007D [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            1A D1                ..
0080: 00 1D 0D 80 23 1D 0E 80  23 21 00                 ....#...#!.     
```

#### Opcodes

```
  0: 0x007E [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x0081 [0x1D] PRINT_EVENT_MESSAGE(message_id=10428*)
    → "<Player>! There's hardly a soul in Norg that doesn't know yer bloody name."
  2: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=10429*)
    → "Oh, sorry 'bout that. Me mum never did teach me no manners. I'll watch me damn mouth...I mean, I'll watch me mouth from now on."
  4: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0089 [0x21] END_EVENT
  6: 0x008A [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   1A D1 00 1D 0F             .....
0090: 80 23 1A 0F 01 1D 10 80  23 1D 11 80 23 21 00     .#......#...#!. 
```

#### Opcodes

```
  0: 0x008B [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=10430*)
    → "<Player>...[Mister/Miss] <Player>. You've become quite the household name 'round Norg."
  2: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0092 [0x1A] CALL_SUBROUTINE(address=0x010F)
  4: 0x0095 [0x1D] PRINT_EVENT_MESSAGE(message_id=10431*)
    → "All me mateys keep askin' me if I can introduce them to ya. You've made quite a reputation for yerself!"
  5: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0099 [0x1D] PRINT_EVENT_MESSAGE(message_id=10432*)
    → "Lookin' at ya gets me thinkin' like I should leave tha life on the open sea, and become an adventurer!"
  7: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x009D [0x21] END_EVENT
  9: 0x009E [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009F  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               1A                 .
00A0: D1 00 1D 12 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x009F [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x00A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10433*)
    → "[Mister/Miss] <Player>! There's already rumors of yer last adventure goin' 'round Norg. You're startin' t'become some sorta legend!"
  2: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A6 [0x21] END_EVENT
  4: 0x00A7 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00A8    |
| Data Size    | 263 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          1A D1 00 1D 13 80 23 66          ......#f
00B0: 14 80 F8 FF FF 7F F8 FF  FF 7F 73 6C 30 30 1D 15  ..........sl00..
00C0: 80 23 53 F8 FF FF 7F F8  FF FF 7F 73 6C 30 30 21  .#S........sl00!
00D0: 00 86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 1B 66  ............op.f
00E0: 16 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
00F0: 16 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 1B 66  ..........tlk1.f
0100: 17 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0110: 03 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0120: 18 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0130: 19 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0140: 1A 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 66  ..........tlk0.f
0150: 1B 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
0160: 1C 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
0170: 1D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
0180: 1E 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
0190: 1F 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1B 5B  ..........tlk0.[
01A0: 1B 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 30 1B     ..........tlb0. 
```

#### Opcodes

```
  0: 0x00A8 [0x1A] CALL_SUBROUTINE(address=0x00D1)
  1: 0x00AB [0x1D] PRINT_EVENT_MESSAGE(message_id=10434*)
    → "[Lord/Lady] <Player>! Next t'our leader, Gilgamesh, yer the most famous person in all'a Norg! Some of me mateys are even callin' ya a hero!"
  2: 0x00AE [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00AF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [EventEntity, EventEntity], work=21*
  4: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=10435*)
    → "May the light of the Dawn Goddess shine down upon ya in all yer journeys 'round Vana'diel!"
  5: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [EventEntity, EventEntity]
  7: 0x00CF [0x21] END_EVENT
  8: 0x00D0 [0x00] END_REQSTACK()

SUBROUTINE_00D1:
  9: 0x00D1 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
 10: 0x00D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
 11: 0x00DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x00DD [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 13: 0x00DE [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
     0x00EE [0x1B] RETURN
     0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
     0x00FE [0x1B] RETURN
     0x00FF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
     0x010E [0x1B] RETURN
     0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
     0x011E [0x1B] RETURN
     0x011F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x012E [0x1B] RETURN
     0x012F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
     0x013E [0x1B] RETURN
     0x013F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
     0x014E [0x1B] RETURN
     0x014F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
     0x015E [0x1B] RETURN
     0x015F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=5*
     0x016E [0x1B] RETURN
     0x016F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
     0x017E [0x1B] RETURN
     0x017F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=238*
     0x018E [0x1B] RETURN
     0x018F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=566*
     0x019E [0x1B] RETURN
     0x019F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=60*
     0x01AE [0x1B] RETURN
```
