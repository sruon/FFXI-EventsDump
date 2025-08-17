# 17797158 - Kotan-Purutan

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 320 bytes        |
| Total Events     | 6                |
| References Count | 9                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [140](#event-140)     | 0x0001       |     73 |             13 |
| [141](#event-141)     | 0x004A       |     82 |             16 |
| [144](#event-144)     | 0x009C       |     32 |             10 |
| [142](#event-142)     | 0x00BC       |     28 |              8 |
| [143](#event-143)     | 0x00D8       |     28 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1BB9      |        7097 |
|       2 | 0x1BBA      |        7098 |
|       3 | 0x1BBC      |        7100 |
|       4 | 0x1BBD      |        7101 |
|       5 | 0x1BBE      |        7102 |
|       6 | 0x03E8      |        1000 |
|       7 | 0x1BBB      |        7099 |
|       8 | 0x1BBF      |        7103 |

## String References

- **7097**: Ah! Are you from the Rhinostery?
- **7098**: You're not? Spitting dhalmels! I wish they would hurry-wurry!
- **7099**: Could you come back when it's dark? I know it's a bother-wother, but I was specifically instructed not to take it out during the day.
- **7100**: Oh, you're the person from the Rhinostery? I've been waiting for you!
- **7101**: I guess it's a really important parcel-morsel. I had to follow all these rules when I was handling it! Thankfully, it's really small, so it was easy to carry.
- **7102**: I hear you have some pretty strict restrictions you have to follow, too. You should leave immediately, and don't get distracted on the way to the Rhinostery!
- **7103**: Ah! Nice to see you again! Did you manage to deliver that parcel-morsel on time?

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

### Event 140

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 73 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 53 F8  ...tlk0...#...S.
0020: FF FF 7F F8 FF FF 7F 74  6C 6B 30 66 00 80 F8 FF  .......tlk0f....
0030: FF 7F F8 FF FF 7F 64 69  73 30 23 53 F8 FF FF 7F  ......dis0#S....
0040: F8 FF FF 7F 64 69 73 30  21 00                    ....dis0!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7097*)
    → "Ah! Are you from the Rhinostery?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7098*)
    → "You're not? Spitting dhalmels! I wish they would hurry-wurry!"
  7: 0x001E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  8: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  9: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
 11: 0x0048 [0x21] END_EVENT
 12: 0x0049 [0x00] END_REQSTACK()
```

### Event 141

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 82 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                1E F0 FF FF 7F 6F            .....o
0050: 70 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  pf..........tlk0
0060: 1D 03 80 23 1D 04 80 23  1D 05 80 53 F8 FF FF 7F  ...#...#...S....
0070: F8 FF FF 7F 74 6C 6B 30  66 00 80 F8 FF FF 7F F8  ....tlk0f.......
0080: FF FF 7F 64 69 73 30 23  53 F8 FF FF 7F F8 FF FF  ...dis0#S.......
0090: 7F 64 69 73 30 03 01 10  06 80 21 00              .dis0.....!.    
```

#### Opcodes

```
  0: 0x004A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0050 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0051 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=7100*)
    → "Oh, you're the person from the Rhinostery? I've been waiting for you!"
  5: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=7101*)
    → "I guess it's a really important parcel-morsel. I had to follow all these rules when I was handling it! Thankfully, it's really small, so it was easy to carry."
  7: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=7102*)
    → "I hear you have some pretty strict restrictions you have to follow, too. You should leave immediately, and don't get distracted on the way to the Rhinostery!"
  9: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 10: 0x0078 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
 11: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0088 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
 13: 0x0095 [0x03] Work_Zone[1] = 1000*
 14: 0x009A [0x21] END_EVENT
 15: 0x009B [0x00] END_REQSTACK()
```

### Event 144

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      1E F0 FF FF              ....
00A0: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
00B0: 6B 30 1D 01 80 23 1D 07  80 23 21 00              k0...#...#!.    
```

#### Opcodes

```
  0: 0x009C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7097*)
    → "Ah! Are you from the Rhinostery?"
  5: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00B6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7099*)
    → "Could you come back when it's dark? I know it's a bother-wother, but I was specifically instructed not to take it out during the day."
  7: 0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00BA [0x21] END_EVENT
  9: 0x00BB [0x00] END_REQSTACK()
```

### Event 142

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      1E F0 FF FF              ....
00C0: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
00D0: 6B 30 1D 05 80 23 21 00                           k0...#!.        
```

#### Opcodes

```
  0: 0x00BC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7102*)
    → "I hear you have some pretty strict restrictions you have to follow, too. You should leave immediately, and don't get distracted on the way to the Rhinostery!"
  5: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D6 [0x21] END_EVENT
  7: 0x00D7 [0x00] END_REQSTACK()
```

### Event 143

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          1E F0 FF FF 7F 6F 70 66          .....opf
00E0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 08  ..........tlk0..
00F0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00D8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00DE [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x00EE [0x1D] PRINT_EVENT_MESSAGE(message_id=7103*)
    → "Ah! Nice to see you again! Did you manage to deliver that parcel-morsel on time?"
  5: 0x00F1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00F2 [0x21] END_EVENT
  7: 0x00F3 [0x00] END_REQSTACK()
```
