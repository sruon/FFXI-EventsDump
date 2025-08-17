# 17105511 - Hauberliond

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 104 bytes                        |
| Total Events     | 8                                |
| References Count | 3                                |

## List of Events

| Event ID          | Entrypoint   |   Size |   Instructions |
|-------------------|--------------|--------|----------------|
| [89](#event-89)   | 0x0000       |      1 |              1 |
| [90](#event-90)   | 0x0001       |      1 |              1 |
| [92](#event-92)   | 0x0002       |     18 |              6 |
| [91](#event-91)   | 0x0014       |     18 |              6 |
| [130](#event-130) | 0x0026       |      1 |              1 |
| [134](#event-134) | 0x0027       |      1 |              1 |
| [140](#event-140) | 0x0028       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x31D8      |       12760 |
|       2 | 0x31D7      |       12759 |

## Events

### Event 89

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

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 92

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 1C  00 80 2B F8 FF FF 7F 01    ........+.....
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x2B] EventEntity [12760*]:
    → "I have been stationed here to watch over the Allied Forces' supply of armaments. Move along, and keep your hands where they belong."
  3: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0012 [0x21] END_EVENT
  5: 0x0013 [0x00] END_REQSTACK()
```

### Event 91

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             1E F0 FF FF  7F 1C 00 80 2B F8 FF FF      ........+...
0020: 7F 02 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0014 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0019 [0x1C] WAIT(30* ticks)
  2: 0x001C [0x2B] EventEntity [12759*]:
    → "We've relocated the supplies to [/East Ronfaure/Jugner Forest/La Vaule]. Should you deem them necessary to your cause, you are welcome to them."
  3: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0024 [0x21] END_EVENT
  5: 0x0025 [0x00] END_REQSTACK()
```

### Event 130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   00                                    .         
```

#### Opcodes

```
  0: 0x0026 [0x00] END_REQSTACK()
```

### Event 134

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 140

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```
