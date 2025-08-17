# 16962104 - Kenapa-Keppa

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 252 bytes                   |
| Total Events     | 7                           |
| References Count | 12                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [350](#event-350)     | 0x0001       |     13 |              7 |
| [351](#event-351)     | 0x000E       |     58 |             18 |
| [352](#event-352)     | 0x0048       |     25 |             13 |
| [353](#event-353)     | 0x0061       |     35 |             11 |
| [354](#event-354)     | 0x0084       |     13 |              7 |
| [355](#event-355)     | 0x0091       |     13 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F1B      |        7963 |
|       1 | 0x1F1C      |        7964 |
|       2 | 0x0151      |         337 |
|       3 | 0x1F1D      |        7965 |
|       4 | 0x1F1E      |        7966 |
|       5 | 0x1F1F      |        7967 |
|       6 | 0x1F20      |        7968 |
|       7 | 0x1F22      |        7970 |
|       8 | 0x1F23      |        7971 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0000      |           0 |
|      11 | 0x1F29      |        7977 |

## String References

- **7963**: Not...safe...here... You...should...go...
- **7964**: What...? You'll...help...us...? Great... Take...this...
- **7965**: South...west...a...thicket... A...cactus... You'll...see...
- **7966**: Use...this... Something...will...come... Maybe...
- **7967**: Bring...it...back...here...
- **7968**: We're...count...ing...on...you...
- **7970**: Truly...remarkable... I...haven't...been...this...excited...in...years...
- **7971**: This...$3...worthless...now... I'll...throw...it...out...
- **7977**: We're...sorry... So...so...sorry...

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

### Event 350

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7963*)
    → "Not...safe...here... You...should...go..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 351

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 58 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            42 1E                B.
0010: F0 FF FF 7F 6F 70 1D 01  80 23 5B 02 80 F8 FF FF  ....op...#[.....
0020: 7F F8 FF FF 7F 70 61 73  30 1D 03 80 23 1D 04 80  .....pas0...#...
0030: 23 1D 05 80 23 1D 06 80  23 53 F8 FF FF 7F F8 FF  #...#...#S......
0040: FF 7F 70 61 73 30 21 00                           ..pas0!.        
```

#### Opcodes

```
  0: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0015 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7964*)
    → "What...? You'll...help...us...? Great... Take...this..."
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=337*
  7: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7965*)
    → "South...west...a...thicket... A...cactus... You'll...see..."
  8: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7966*)
    → "Use...this... Something...will...come... Maybe..."
 10: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "Bring...it...back...here..."
 12: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "We're...count...ing...on...you..."
 14: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0039 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 16: 0x0046 [0x21] END_EVENT
 17: 0x0047 [0x00] END_REQSTACK()
```

### Event 352

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 25 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0050: 03 80 23 1D 04 80 23 1D  05 80 23 1D 06 80 23 21  ..#...#...#...#!
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7965*)
    → "South...west...a...thicket... A...cactus... You'll...see..."
  4: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7966*)
    → "Use...this... Something...will...come... Maybe..."
  6: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "Bring...it...back...here..."
  8: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "We're...count...ing...on...you..."
 10: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x005F [0x21] END_EVENT
 12: 0x0060 [0x00] END_REQSTACK()
```

### Event 353

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 35 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    42 1E F0 FF FF 7F 6F  70 1D 07 80 23 1D 08 80   B.....op...#...
0070: 23 45 09 80 F0 FF FF 7F  F0 FF FF 7F 71 73 74 63  #E..........qstc
0080: 0A 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0061 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0068 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "Truly...remarkable... I...haven't...been...this...excited...in...years..."
  5: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "This...$3...worthless...now... I'll...throw...it...out..."
  7: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0071 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  9: 0x0082 [0x21] END_EVENT
 10: 0x0083 [0x00] END_REQSTACK()
```

### Event 354

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             1E F0 FF FF  7F 6F 70 1D 07 80 23 21      .....op...#!
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0084 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x008A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x008B [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "Truly...remarkable... I...haven't...been...this...excited...in...years..."
  4: 0x008E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x008F [0x21] END_EVENT
  6: 0x0090 [0x00] END_REQSTACK()
```

### Event 355

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    1E F0 FF FF 7F 6F 70  1D 0B 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0091 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0096 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0097 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "We're...sorry... So...so...sorry..."
  4: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009C [0x21] END_EVENT
  6: 0x009D [0x00] END_REQSTACK()
```
