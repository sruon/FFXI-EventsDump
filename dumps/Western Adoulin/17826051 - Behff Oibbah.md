# 17826051 - Behff Oibbah

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 424 bytes                 |
| Total Events     | 9                         |
| References Count | 27                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [514](#event-514)        | 0x0001       |     47 |             11 |
| [2](#event-2)            | 0x0030       |      1 |              1 |
| [65535.1](#event-655351) | 0x0031       |     24 |              3 |
| [65535.2](#event-655352) | 0x0049       |     15 |              5 |
| [65535.3](#event-655353) | 0x0058       |     15 |              5 |
| [65535.4](#event-655354) | 0x0067       |     22 |              6 |
| [65535.5](#event-655355) | 0x007D       |    112 |             16 |
| [65535.6](#event-655356) | 0x00ED       |     24 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0035      |          53 |
|       1 | 0x267D      |        9853 |
|       2 | 0x267E      |        9854 |
|       3 | 0x0007      |           7 |
|       4 | 0x000D      |          13 |
|       5 | 0x0000      |           0 |
|       6 | 0x0010      |          16 |
|       7 | 0x0001      |           1 |
|       8 | 0x0804      |        2052 |
|       9 | 0xFFFFEAE7  |  4294961895 |
|      10 | 0x617EE     |      399342 |
|      11 | 0xFFFFE340  |  4294959936 |
|      12 | 0x0FA0      |        4000 |
|      13 | 0xFFFE7BA1  |  4294867873 |
|      14 | 0xFFFFC4C5  |  4294952133 |
|      15 | 0x0C00      |        3072 |
|      16 | 0xFFFD564A  |  4294792778 |
|      17 | 0xFFFFBD49  |  4294950217 |
|      18 | 0x0F9F      |        3999 |
|      19 | 0x0013      |          19 |
|      20 | 0x000F      |          15 |
|      21 | 0x0032      |          50 |
|      22 | 0x004B      |          75 |
|      23 | 0x001E      |          30 |
|      24 | 0x00E1      |         225 |
|      25 | 0x00D6      |         214 |
|      26 | 0x0003      |           3 |

## String References

- **9853**: You ever hear about rrrune fencers?
- **9854**: They're accomplished sworrrdsmen who make use of runes to snuff out their enemies and empower their friends. Their techniques may have been passed down through the Order of Orvail for generrrations, but even I could use them if I stopped catting around for once.

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

### Event 514

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 31 1D  01 80 23 1D 02 80 23 66  ...tlb1...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 32 21 00  ..........tlb2!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9853*)
    → "You ever hear about rrrune fencers?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9854*)
    → "They're accomplished sworrrdsmen who make use of runes to snuff out their enemies and empower their friends. Their techniques may have been passed down through the Order of Orvail for generrrations, but even I could use them if I stopped catting around for once."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    B6 0B 03 80 04 80 05  80 06 80 06 80 06 80 06   ...............
0040: 80 05 80 05 80 C0 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x0031 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=0*, body=16*, hands=16*, legs=16*, feet=16*, main=0*, sub=0*)
  1: 0x0045 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             32 04 80 1F 00 08 80           2......
0050: 09 80 05 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0049 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=2.052*, Z=-5.401*, Y=0.000*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 04 80 1F 00 0A 80 0B          2.......
0060: 80 0C 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=399.342*, Z=-7.360*, Y=4.000*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  04 80 1F 00 0D 80 0E 80         2........
0070: 0C 80 1F 01 6F 4B F8 FF  FF 7F 0F 80 00           ....oK.......   
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.423*, Z=-15.163*, Y=4.000*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=16.9°*)
  5: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x007D    |
| Data Size    | 112 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         32 04 80               2..
0080: 1F 00 10 80 11 80 12 80  1F 01 6F 4A 03 01 10 01  ..........oJ....
0090: 93 00 10 01 7B 03 01 10  01 66 13 80 93 00 10 01  ....{....f......
00A0: 93 00 10 01 74 6C 73 31  1C 14 80 66 15 80 03 01  ....tls1...f....
00B0: 10 01 03 01 10 01 74 6C  6B 30 1C 16 80 66 15 80  ......tlk0...f..
00C0: 03 01 10 01 03 01 10 01  74 6C 6B 32 4A 03 01 10  ........tlk2J...
00D0: 01 93 00 10 01 7B 03 01  10 01 1C 17 80 66 13 80  .....{.......f..
00E0: 93 00 10 01 93 00 10 01  74 6C 73 30 00           ........tls0.   
```

#### Opcodes

```
  0: 0x007D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=-174.518*, Z=-17.079*, Y=3.999*
  2: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008B [0x4A] Behff Oibbah (ID: 17826051/0x01100103) looks at Brenna (ID: 17825939/0x01100093)
  5: 0x0094 [0x7B] Behff Oibbah (ID: 17826051/0x01100103) stops talking
  6: 0x0099 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tls1" with entities [Brenna (ID: 17825939/0x01100093), Brenna (ID: 17825939/0x01100093)], work=19*
  7: 0x00A8 [0x1C] WAIT(15* ticks)
  8: 0x00AB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Behff Oibbah (ID: 17826051/0x01100103), Behff Oibbah (ID: 17826051/0x01100103)], work=50*
  9: 0x00BA [0x1C] WAIT(75* ticks)
 10: 0x00BD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [Behff Oibbah (ID: 17826051/0x01100103), Behff Oibbah (ID: 17826051/0x01100103)], work=50*
 11: 0x00CC [0x4A] Behff Oibbah (ID: 17826051/0x01100103) looks at Brenna (ID: 17825939/0x01100093)
 12: 0x00D5 [0x7B] Behff Oibbah (ID: 17826051/0x01100103) stops talking
 13: 0x00DA [0x1C] WAIT(30* ticks)
 14: 0x00DD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tls0" with entities [Brenna (ID: 17825939/0x01100093), Brenna (ID: 17825939/0x01100093)], work=19*
 15: 0x00EC [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         B6 0B 03               ...
00F0: 80 04 80 05 80 18 80 18  80 19 80 1A 80 05 80 05  ................
0100: 80 C0 07 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00ED [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=0*, body=225*, hands=225*, legs=214*, feet=3*, main=0*, sub=0*)
  1: 0x0101 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0104 [0x00] END_REQSTACK()
```
