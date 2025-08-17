# 17481823 - Drake Fang

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Zeruhn Mines (ID: 172) |
| Block Size       | 108 bytes              |
| Total Events     | 8                      |
| References Count | 4                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [108](#event-108)     | 0x0001       |     11 |              5 |
| [200](#event-200)     | 0x000C       |      1 |              1 |
| [201](#event-201)     | 0x000D       |     16 |              6 |
| [202](#event-202)     | 0x001D       |      1 |              1 |
| [203](#event-203)     | 0x001E       |     11 |              5 |
| [204](#event-204)     | 0x0029       |      1 |              1 |
| [226](#event-226)     | 0x002A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA2      |        7330 |
|       1 | 0x010A      |         266 |
|       2 | 0x1CDA      |        7386 |
|       3 | 0x1CE5      |        7397 |

## String References

- **7330**: Shipments of mythril used to be ferried to this dock from the Palborough Mines, but it's been closed off since the Quadav took Palborough.
- **7386**: If you happen to find $6, take it to Tall Mountain, a guard in the off-limits area in the Mines District.
- **7397**: When you find proof of Werei's journey, bring it here. I'll be waiting for you.

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

### Event 108

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7330*)
    → "Shipments of mythril used to be ferried to this dock from the Palborough Mines, but it's been closed off since the Quadav took Palborough."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         03 09 10               ...
0010: 01 80 1E F0 FF FF 7F 1D  02 80 23 21 00           ..........#!.   
```

#### Opcodes

```
  0: 0x000D [0x03] Work_Zone[9] = 266*
  1: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7386*)
    → "If you happen to find $6, take it to Tall Mountain, a guard in the off-limits area in the Mines District."
  3: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001B [0x21] END_EVENT
  5: 0x001C [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 1D 03 80 23 21  00                       ......#!.       
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7397*)
    → "When you find proof of Werei's journey, bring it here. I'll be waiting for you."
  2: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0027 [0x21] END_EVENT
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 226

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```
