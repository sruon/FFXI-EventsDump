# 17428916 - Tome of Magic

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 64 bytes                      |
| Total Events     | 2                             |
| References Count | 4                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [21](#event-21)       | 0x0001       |     20 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CE5      |        7397 |
|       1 | 0x1CE6      |        7398 |
|       2 | 0x1CE7      |        7399 |
|       3 | 0x1CE8      |        7400 |

## String References

- **7397**: A diary written by Iru-Kuiru.
- **7398**: "A letter has arrived from the homeland. The San d'Orian member of the Allied Expedition, Francmage M Mistalle, has lost his life to the curse..."
- **7399**: "And then yesterday, my friend and fellow Allied explorer, Yow Rabntah, was taken from this world..."
- **7400**: "I can feel the shadow closing in on me. I believe the darkness will claim me before I am able to finish this research. And I was so close to putting all the pieces of this legend together..."

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

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 1D 02 80 23 1D 03 80   ...#...#...#...
0010: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7397*)
    → "A diary written by Iru-Kuiru."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7398*)
    → ""A letter has arrived from the homeland. The San d'Orian member of the Allied Expedition, Francmage M Mistalle, has lost his life to the curse...""
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7399*)
    → ""And then yesterday, my friend and fellow Allied explorer, Yow Rabntah, was taken from this world...""
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=7400*)
    → ""I can feel the shadow closing in on me. I believe the darkness will claim me before I am able to finish this research. And I was so close to putting all the pieces of this legend together...""
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0013 [0x21] END_EVENT
 10: 0x0014 [0x00] END_REQSTACK()
```
