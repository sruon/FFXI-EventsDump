# 17752231 - DoorCulinarians Guild

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 76 bytes                  |
| Total Events     | 6                         |
| References Count | 0                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [978](#event-978)     | 0x0001       |      8 |              3 |
| [983](#event-983)     | 0x0009       |      8 |              3 |
| [980](#event-980)     | 0x0011       |      8 |              3 |
| [981](#event-981)     | 0x0019       |      8 |              3 |
| [1069](#event-1069)   | 0x0021       |      1 |              1 |

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

### Event 978

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 4D  00                        ......M.       
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x4D] EventEntity->StatusEvent = 9 // Close door
  2: 0x0008 [0x00] END_REQSTACK()
```

### Event 983

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             92 01 F8 FF FF 7F 4D           ......M
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000F [0x4D] EventEntity->StatusEvent = 9 // Close door
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 980

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    92 01 F8 FF FF 7F 4D  00                        ......M.       
```

#### Opcodes

```
  0: 0x0011 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0017 [0x4D] EventEntity->StatusEvent = 9 // Close door
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 981

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             4D 92 01 F8 FF FF 7F           M......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0019 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 1069

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    00                                              .              
```

#### Opcodes

```
  0: 0x0021 [0x00] END_REQSTACK()
```
