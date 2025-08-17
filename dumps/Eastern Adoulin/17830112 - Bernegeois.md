# 17830112 - Bernegeois

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 260 bytes                 |
| Total Events     | 18                        |
| References Count | 4                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5032](#event-5032)      | 0x0001       |      7 |              2 |
| [5097](#event-5097)      | 0x0008       |      7 |              2 |
| [5099](#event-5099)      | 0x000F       |      7 |              2 |
| [5102](#event-5102)      | 0x0016       |      7 |              2 |
| [5124](#event-5124)      | 0x001D       |      7 |              2 |
| [5130](#event-5130)      | 0x0024       |      7 |              2 |
| [5202](#event-5202)      | 0x002B       |      7 |              2 |
| [106](#event-106)        | 0x0032       |      7 |              2 |
| [5212](#event-5212)      | 0x0039       |      7 |              2 |
| [5214](#event-5214)      | 0x0040       |      7 |              2 |
| [5217](#event-5217)      | 0x0047       |      7 |              2 |
| [5222](#event-5222)      | 0x004E       |      7 |              2 |
| [115](#event-115)        | 0x0055       |      7 |              2 |
| [120](#event-120)        | 0x005C       |      7 |              2 |
| [65535.1](#event-655351) | 0x0063       |      4 |              2 |
| [65535.2](#event-655352) | 0x0067       |      2 |              2 |
| [83](#event-83)          | 0x0069       |     48 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001B      |          27 |
|       2 | 0x2D96      |       11670 |
|       3 | 0x2D97      |       11671 |

## String References

- **11670**: A fine day to you, [sir/madam]. I trust you are here about a particular set of customers' tabs?
- **11671**: Thank you for your payment. We look forward to serving other members of the Mummers' Coalition.

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

### Event 5032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 5097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 5099

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               92                 .
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 5102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 5124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         92 01 F8               ...
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 5130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0024 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 5202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   92 01 F8 FF FF             .....
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x002B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0032 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 5212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0039 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 5214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0040 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 5217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0047 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 5222

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            92 01                ..
0050: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x004E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0055 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      92 01 F8 FF              ....
0060: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x005C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          95 00 80 00                                 ....         
```

#### Opcodes

```
  0: 0x0063 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      96  00                              ..       
```

#### Opcodes

```
  0: 0x0067 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 83

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             42 1E F0 FF FF 7F 6F           B.....o
0070: 70 66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 62 30  pf..........tlb0
0080: 1D 02 80 23 1D 03 80 23  66 01 80 F8 FF FF 7F F8  ...#...#f.......
0090: FF FF 7F 74 6C 62 31 21  00                       ...tlb1!.       
```

#### Opcodes

```
  0: 0x0069 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0070 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0071 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  5: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=11670*)
    → "A fine day to you, [sir/madam]. I trust you are here about a particular set of customers' tabs?"
  6: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=11671*)
    → "Thank you for your payment. We look forward to serving other members of the Mummers' Coalition."
  8: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0088 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
 10: 0x0097 [0x21] END_EVENT
 11: 0x0098 [0x00] END_REQSTACK()
```
