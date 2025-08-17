# 17670775 - Ronta-Onta

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
| [344](#event-344)     | 0x0001       |     18 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2069      |        8297 |
|       1 | 0x0014      |          20 |
|       2 | 0x206A      |        8298 |

## String References

- **8297**: Owzie-wowzie! Don't make me talk. I hurt all over!
- **8298**: Still, I'm glad to see you alive and kicking-wicking. Have you heard about my friend? I do hope he's okay too...

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

### Event 344

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1E F0 FF  FF 7F 1C 01 80 1D 02 80   ...#...........
0010: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=8297*)
    → "Owzie-wowzie! Don't make me talk. I hurt all over!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x1C] WAIT(20* ticks)
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=8298*)
    → "Still, I'm glad to see you alive and kicking-wicking. Have you heard about my friend? I do hope he's okay too..."
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x21] END_EVENT
  7: 0x0012 [0x00] END_REQSTACK()
```
