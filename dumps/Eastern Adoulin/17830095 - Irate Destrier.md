# 17830095 - Irate Destrier

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 364 bytes                 |
| Total Events     | 20                        |
| References Count | 11                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [505](#event-505)        | 0x0001       |     43 |              9 |
| [2515](#event-2515)      | 0x002C       |     72 |             24 |
| [5032](#event-5032)      | 0x0074       |      7 |              2 |
| [5097](#event-5097)      | 0x007B       |      7 |              2 |
| [5099](#event-5099)      | 0x0082       |      7 |              2 |
| [5102](#event-5102)      | 0x0089       |      7 |              2 |
| [5124](#event-5124)      | 0x0090       |      7 |              2 |
| [5130](#event-5130)      | 0x0097       |      7 |              2 |
| [5202](#event-5202)      | 0x009E       |      7 |              2 |
| [106](#event-106)        | 0x00A5       |      7 |              2 |
| [5212](#event-5212)      | 0x00AC       |      7 |              2 |
| [5214](#event-5214)      | 0x00B3       |      7 |              2 |
| [5217](#event-5217)      | 0x00BA       |      7 |              2 |
| [5222](#event-5222)      | 0x00C1       |      7 |              2 |
| [115](#event-115)        | 0x00C8       |      7 |              2 |
| [120](#event-120)        | 0x00CF       |      7 |              2 |
| [65535.1](#event-655351) | 0x00D6       |      4 |              2 |
| [65535.2](#event-655352) | 0x00DA       |      2 |              2 |
| [5132](#event-5132)      | 0x00DC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0041      |          65 |
|       1 | 0x28C6      |       10438 |
|       2 | 0x1ED0      |        7888 |
|       3 | 0x1ED1      |        7889 |
|       4 | 0x1ED2      |        7890 |
|       5 | 0x1ED3      |        7891 |
|       6 | 0x1ED4      |        7892 |
|       7 | 0x1ED5      |        7893 |
|       8 | 0x1ED6      |        7894 |
|       9 | 0x1ED7      |        7895 |
|      10 | 0x0000      |           0 |

## String References

- **7888**: Did something happen? What brings you here?
- **7889**: Making the rounds? That idiot must've sent you, then.
- **7890**: As you can see, everything here is the picture of peace itself. When you've got someone as competent as me, there's no way anything could go wrong.
- **7891**: This is where people in Eastern Adoulin come to relax. If it's not safe here, it's not safe anywhere!
- **7892**: The citizenry offers prayers to Altana and enjoys cups of tea while gazing over the plaza. It's quite a lovely area.
- **7893**: On clear mornings, you can see the newborn sun rising over Castle Adoulin.
- **7894**: Sometimes residents wake up early just to witness the spectacle.
- **7895**: Forgive my ramblings. You have a mission to complete, don't you?
- **10438**: We, the Peacekeepers' Coalition, are here to serve and protect the citizens of Adoulin! Outsiders like you wouldn't know the first thing about how to keep Adoulin safe from...well...the outside!

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

### Event 505

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 30 1D  01 80 23 66 00 80 F8 FF  ...tlb0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  62 31 21 00              ......tlb1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10438*)
    → "We, the Peacekeepers' Coalition, are here to serve and protect the citizens of Adoulin! Outsiders like you wouldn't know the first thing about how to keep Adoulin safe from...well...the outside!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 2515

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 72 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      1E F0 FF FF              ....
0030: 7F 42 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  .Bopf..........t
0040: 6C 62 30 1D 02 80 23 1D  03 80 23 1D 04 80 23 1D  lb0...#...#...#.
0050: 05 80 23 1D 06 80 23 1D  07 80 23 1D 08 80 23 1D  ..#...#...#...#.
0060: 09 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0070: 62 31 21 00                                       b1!.            
```

#### Opcodes

```
  0: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0031 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  5: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=7888*)
    → "Did something happen? What brings you here?"
  6: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=7889*)
    → "Making the rounds? That idiot must've sent you, then."
  8: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7890*)
    → "As you can see, everything here is the picture of peace itself. When you've got someone as competent as me, there's no way anything could go wrong."
 10: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7891*)
    → "This is where people in Eastern Adoulin come to relax. If it's not safe here, it's not safe anywhere!"
 12: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7892*)
    → "The citizenry offers prayers to Altana and enjoys cups of tea while gazing over the plaza. It's quite a lovely area."
 14: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7893*)
    → "On clear mornings, you can see the newborn sun rising over Castle Adoulin."
 16: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=7894*)
    → "Sometimes residents wake up early just to witness the spectacle."
 18: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7895*)
    → "Forgive my ramblings. You have a mission to complete, don't you?"
 20: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
 22: 0x0072 [0x21] END_EVENT
 23: 0x0073 [0x00] END_REQSTACK()
```

### Event 5032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0074 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 5097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   92 01 F8 FF FF             .....
0080: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x007B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0081 [0x00] END_REQSTACK()
```

### Event 5099

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0082 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 5102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0089  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0089 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008F [0x00] END_REQSTACK()
```

### Event 5124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0090  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0090 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 5130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0097 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x009D [0x00] END_REQSTACK()
```

### Event 5202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            92 01                ..
00A0: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x009E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x00A5 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 5212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AC  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      92 01 F8 FF              ....
00B0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00AC [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B2 [0x00] END_REQSTACK()
```

### Event 5214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B3  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x00B3 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B9 [0x00] END_REQSTACK()
```

### Event 5217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BA  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                92 01 F8 FF FF 7F            ......
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00BA [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C0 [0x00] END_REQSTACK()
```

### Event 5222

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C1  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x00C1 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C7 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C8  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x00C8 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00CE [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CF  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               92                 .
00D0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00CF [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D6  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   95 0A  80 00                          ....      
```

#### Opcodes

```
  0: 0x00D6 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DA  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                96 00                        ..    
```

#### Opcodes

```
  0: 0x00DA [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x00DB [0x00] END_REQSTACK()
```

### Event 5132

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00DC [0x00] END_REQSTACK()
```
