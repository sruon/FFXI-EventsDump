# 17830097 - Alphonserme

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 332 bytes                 |
| Total Events     | 19                        |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [507](#event-507)        | 0x0001       |     51 |             13 |
| [5045](#event-5045)      | 0x0034       |     56 |             12 |
| [5032](#event-5032)      | 0x006C       |      7 |              2 |
| [5097](#event-5097)      | 0x0073       |      7 |              2 |
| [5099](#event-5099)      | 0x007A       |      7 |              2 |
| [5102](#event-5102)      | 0x0081       |      7 |              2 |
| [5124](#event-5124)      | 0x0088       |      7 |              2 |
| [5130](#event-5130)      | 0x008F       |      7 |              2 |
| [5202](#event-5202)      | 0x0096       |      7 |              2 |
| [106](#event-106)        | 0x009D       |      7 |              2 |
| [5212](#event-5212)      | 0x00A4       |      7 |              2 |
| [5214](#event-5214)      | 0x00AB       |      7 |              2 |
| [5217](#event-5217)      | 0x00B2       |      7 |              2 |
| [5222](#event-5222)      | 0x00B9       |      7 |              2 |
| [115](#event-115)        | 0x00C0       |      7 |              2 |
| [120](#event-120)        | 0x00C7       |      7 |              2 |
| [65535.1](#event-655351) | 0x00CE       |      4 |              2 |
| [65535.2](#event-655352) | 0x00D2       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x28D8      |       10456 |
|       2 | 0x28D9      |       10457 |
|       3 | 0x28DA      |       10458 |
|       4 | 0x28B5      |       10421 |
|       5 | 0x28B6      |       10422 |
|       6 | 0x0000      |           0 |

## String References

- **10421**: The seas have been quite rough as of late. I cannot imagine anyone making their way to the Yahse Hunting Grounds via ship without the help of a map to delineate the currents.
- **10422**: Of course, our white cap-hardened captain is more knowledgeable about these waters than everyone on the continent. Do not forget to thank him for his lifesaving expertise should you seek passage on his vessel.
- **10456**: Stroll northwards and you shall meet with a wharf that docks ferries bound for the Yahse Hunting Grounds.
- **10457**: Hahaha, your concern about sea monsters wreaking havoc on Adoulin is certainly a logical one to have. I myself consider the Peacekeepers no more than jesters dressed in steel rather than motley.
- **10458**: Yet, praise be to Altana, such a dreadful event has yet to occur.

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

### Event 507

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
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 1D  ...tlk0...#...#.
0020: 03 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0030: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10456*)
    → "Stroll northwards and you shall meet with a wharf that docks ferries bound for the Yahse Hunting Grounds."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10457*)
    → "Hahaha, your concern about sea monsters wreaking havoc on Adoulin is certainly a logical one to have. I myself consider the Peacekeepers no more than jesters dressed in steel rather than motley."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=10458*)
    → "Yet, praise be to Altana, such a dreadful event has yet to occur."
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 11: 0x0032 [0x21] END_EVENT
 12: 0x0033 [0x00] END_REQSTACK()
```

### Event 5045

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 56 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             4A F0 FF FF  7F F8 FF FF 7F 1E F0 FF      J...........
0040: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0050: 6C 6B 30 1D 04 80 23 1D  05 80 23 66 00 80 F8 FF  lk0...#...#f....
0060: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0034 [0x4A] LocalPlayer looks at EventEntity
  1: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0043 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=10421*)
    → "The seas have been quite rough as of late. I cannot imagine anyone making their way to the Yahse Hunting Grounds via ship without the help of a map to delineate the currents."
  6: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=10422*)
    → "Of course, our white cap-hardened captain is more knowledgeable about these waters than everyone on the continent. Do not forget to thank him for his lifesaving expertise should you seek passage on his vessel."
  8: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 10: 0x006A [0x21] END_EVENT
 11: 0x006B [0x00] END_REQSTACK()
```

### Event 5032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      92 01 F8 FF              ....
0070: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x006C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 5097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0073  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0073 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 5099

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                92 01 F8 FF FF 7F            ......
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x007A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 5102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0081  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0081 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 5124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0088  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0088 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008E [0x00] END_REQSTACK()
```

### Event 5130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               92                 .
0090: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x008F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0095 [0x00] END_REQSTACK()
```

### Event 5202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0096  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0096 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         92 01 F8               ...
00A0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x009D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 5212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x00A4 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AA [0x00] END_REQSTACK()
```

### Event 5214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   92 01 F8 FF FF             .....
00B0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x00AB [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B1 [0x00] END_REQSTACK()
```

### Event 5217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B2  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x00B2 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B8 [0x00] END_REQSTACK()
```

### Event 5222

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B9  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x00B9 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C0  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00C0 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C6 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C7  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x00C7 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CE  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            95 06                ..
00D0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00CE [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D2  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       96 00                                         ..            
```

#### Opcodes

```
  0: 0x00D2 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x00D3 [0x00] END_REQSTACK()
```
