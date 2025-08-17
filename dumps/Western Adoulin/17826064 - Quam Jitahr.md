# 17826064 - Quam Jitahr

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 252 bytes                 |
| Total Events     | 15                        |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [534](#event-534)        | 0x0001       |     51 |             13 |
| [573](#event-573)        | 0x0034       |     43 |              9 |
| [8](#event-8)            | 0x005F       |      1 |              1 |
| [134](#event-134)        | 0x0060       |      1 |              1 |
| [5043](#event-5043)      | 0x0061       |      1 |              1 |
| [5044](#event-5044)      | 0x0062       |      1 |              1 |
| [5064](#event-5064)      | 0x0063       |      1 |              1 |
| [5065](#event-5065)      | 0x0064       |      1 |              1 |
| [5092](#event-5092)      | 0x0065       |      7 |              2 |
| [65535.1](#event-655351) | 0x006C       |      4 |              2 |
| [65535.2](#event-655352) | 0x0070       |      2 |              2 |
| [65535.3](#event-655353) | 0x0072       |     13 |              3 |
| [65535.4](#event-655354) | 0x007F       |     13 |              3 |
| [5221](#event-5221)      | 0x008C       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0035      |          53 |
|       1 | 0x26B0      |        9904 |
|       2 | 0x26B1      |        9905 |
|       3 | 0x26B2      |        9906 |
|       4 | 0x0000      |           0 |
|       5 | 0x0026      |          38 |
|       6 | 0x001D      |          29 |

## String References

- **9904**: Welcome to the Mummers' Coalition, where the pleasure and prrrosperity of Adoulin's people is our number one goal.
- **9905**: <Sniff>... Aha! I can smell the adventurer on you from a malm away. Then you should rrregister as a pioneer while you're here.
- **9906**: Hightail it over to the Pioneers' Coalition just down the rrroad and speak with Brenton. He'll get you all grrroomed and ready to help colonize the continent!

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

### Event 534

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 51 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 31 1D  01 80 23 1D 02 80 23 1D  ...tlb1...#...#.
0020: 03 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0030: 62 32 21 00                                       b2!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9904*)
    → "Welcome to the Mummers' Coalition, where the pleasure and prrrosperity of Adoulin's people is our number one goal."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9905*)
    → "<Sniff>... Aha! I can smell the adventurer on you from a malm away. Then you should rrregister as a pioneer while you're here."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=9906*)
    → "Hightail it over to the Pioneers' Coalition just down the rrroad and speak with Brenton. He'll get you all grrroomed and ready to help colonize the continent!"
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```

### Event 573

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             1E F0 FF FF  7F 6F 70 66 00 80 F8 FF      .....opf....
0040: FF 7F F8 FF FF 7F 74 6C  62 31 1D 01 80 23 66 00  ......tlb1...#f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 32 21 00     .........tlb2!. 
```

#### Opcodes

```
  0: 0x0034 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0039 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  4: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=9904*)
    → "Welcome to the Mummers' Coalition, where the pleasure and prrrosperity of Adoulin's people is our number one goal."
  5: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  7: 0x005D [0x21] END_EVENT
  8: 0x005E [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 134

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0060 [0x00] END_REQSTACK()
```

### Event 5043

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0061  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    00                                              .              
```

#### Opcodes

```
  0: 0x0061 [0x00] END_REQSTACK()
```

### Event 5044

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       00                                            .             
```

#### Opcodes

```
  0: 0x0062 [0x00] END_REQSTACK()
```

### Event 5064

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 5065

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```

### Event 5092

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0065 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006C  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      95 04 80 00              ....
```

#### Opcodes

```
  0: 0x006C [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 96 00                                             ..              
```

#### Opcodes

```
  0: 0x0070 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       6E F8 FF FF 7F 05  80 99 F8 FF FF 7F 00       n............ 
```

#### Opcodes

```
  0: 0x0072 [0x6E] EventEntity uses emote 38*
  1: 0x0079 [0x99] Wait for EventEntity animation to complete
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               6E                 n
0080: F8 FF FF 7F 06 80 99 F8  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x007F [0x6E] EventEntity uses emote 29*
  1: 0x0086 [0x99] Wait for EventEntity animation to complete
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 5221

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      92 01 F8 FF              ....
0090: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x008C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0092 [0x00] END_REQSTACK()
```
