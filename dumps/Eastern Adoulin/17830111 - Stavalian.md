# 17830111 - Stavalian

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 192 bytes                 |
| Total Events     | 16                        |
| References Count | 2                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [533](#event-533)     | 0x0001       |     10 |              6 |
| [5032](#event-5032)   | 0x000B       |      7 |              2 |
| [5097](#event-5097)   | 0x0012       |      7 |              2 |
| [5099](#event-5099)   | 0x0019       |      7 |              2 |
| [5102](#event-5102)   | 0x0020       |      7 |              2 |
| [5124](#event-5124)   | 0x0027       |      7 |              2 |
| [5130](#event-5130)   | 0x002E       |      7 |              2 |
| [5202](#event-5202)   | 0x0035       |      7 |              2 |
| [106](#event-106)     | 0x003C       |      7 |              2 |
| [5212](#event-5212)   | 0x0043       |      7 |              2 |
| [5214](#event-5214)   | 0x004A       |      7 |              2 |
| [5217](#event-5217)   | 0x0051       |      7 |              2 |
| [5222](#event-5222)   | 0x0058       |      7 |              2 |
| [90](#event-90)       | 0x005F       |      1 |              1 |
| [133](#event-133)     | 0x0060       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28D2      |       10450 |
|       1 | 0x28D3      |       10451 |

## String References

- **10450**: It takes a certain type of genius to sketch a jungle landscape.
- **10451**: That's why I must focus all my creative energy into a dense ball of concentration. I need my muse to descend from the heavens and set my spirit on fire with a volcanic eruption of inspiration!

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

### Event 533

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 21 00                  ...#...#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=10450*)
    → "It takes a certain type of genius to sketch a jungle landscape."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=10451*)
    → "That's why I must focus all my creative energy into a dense ball of concentration. I need my muse to descend from the heavens and set my spirit on fire with a volcanic eruption of inspiration!"
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x21] END_EVENT
  5: 0x000A [0x00] END_REQSTACK()
```

### Event 5032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   92 01 F8 FF FF             .....
0010: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x000B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 5097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0012 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 5099

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0019 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 5102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0020 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 5124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0027 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 5130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            92 01                ..
0030: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x002E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 5202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0035 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      92 01 F8 FF              ....
0040: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x003C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 5212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0043 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 5214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                92 01 F8 FF FF 7F            ......
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x004A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 5217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0051 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 5222

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0058  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0058 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 90

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

### Event 133

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0060 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0066 [0x00] END_REQSTACK()
```
