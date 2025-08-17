# 17670772 - Yuhito-Kubhito

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Abyssea - Altepa (ID: 218) |
| Block Size       | 56 bytes                   |
| Total Events     | 2                          |
| References Count | 3                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [341](#event-341)     | 0x0001       |     18 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2067      |        8295 |
|       2 | 0x2068      |        8296 |

## String References

- **8295**: The counterattack that Minister Ajido-Marujido launched against the fiends was truly a sightaru to behold. It was the first time I saw the full scope of his power...
- **8296**: And yet, in the end, it wasn't enough to save us. What's more, I fear the horror-worrors of that day have left him a broken man...

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

### Event 341

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 1D 02 80   ...........#...
0010: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(20* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=8295*)
    → "The counterattack that Minister Ajido-Marujido launched against the fiends was truly a sightaru to behold. It was the first time I saw the full scope of his power..."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8296*)
    → "And yet, in the end, it wasn't enough to save us. What's more, I fear the horror-worrors of that day have left him a broken man..."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x21] END_EVENT
  7: 0x0012 [0x00] END_REQSTACK()
```
